import random
import json
from functools import reduce

from .Robot import Robot
from .Encuentro import Encuentro
from .Ronda import Ronda

def generador_samu(robots):
    if len(robots) == 2:
        return [Encuentro(robots[0], robots[1])]
    
    _escuela = robots[0].escuela
    _neutros = [r for r in robots if r.escuela==_escuela]
    random.shuffle(_neutros)
    
    _contrincantes = [r for r in robots if r.escuela!=_escuela]
    random.shuffle(_contrincantes)

    _rob_1 = _neutros[0]
    _encuentros = []
    if len(_contrincantes) !=0:
        _rob_2 = _contrincantes[0]
    else:
        _rob_2 = _neutros[1]
    
    robots.remove(_rob_1)
    robots.remove(_rob_2)
    _encuentros.append(Encuentro(_rob_1, _rob_2))
    
    _encuentros.extend(generador_samu(robots))
    
    return _encuentros

def generador_brutus(robots):
    # Producto cartesiano de todos los robots con todos los robots
    encuentros = [Encuentro(r1, r2) for r1 in robots for r2 in robots]
    # Lo barajamos
    random.shuffle(encuentros)
    # Filtramos los que son validos
    encuentros = [encuentro for encuentro in encuentros if encuentro.es_valido()]
    # Filtramos los iguales
    encuentros = reduce(lambda acumulador, encuentro: encuentro in acumulador and acumulador or acumulador + [encuentro], encuentros, [])
    # Quitar los que compite la misma escuela, solo si hay un numero suficiente de encuentros
    encuentros_distintos = [encuentro for encuentro in encuentros if not encuentro.misma_escuela()]
    if len(encuentros_distintos) > len(robots) // 2:
        encuentros = encuentros_distintos
    # Filtramos los encuentros por robot y generamos la ronda
    ronda = []
    _robots = robots[:]
    while _robots:
        encuentro = encuentros.pop()
        if encuentro.robot_1 in _robots and encuentro.robot_2 in _robots:
            _robots.remove(encuentro.robot_1)
            _robots.remove(encuentro.robot_2)
            ronda.append(encuentro)
        elif not encuentros:
            ronda.append(encuentro)
            break
    return ronda

def generador_combinaciones(robots):
    def potencia(c):
        if len(c) == 0:
            return [[]]
        r = potencia(c[:-1])
        return r + [s + [c[-1]] for s in r]

    def combinaciones(rs, n):
        return [s for s in potencia(rs) if len(s) == n]

    tuplas = combinaciones(robots, 2)
    ronda = []
    random.shuffle(tuplas)
    distinta_escuela = [ e for e in tuplas if e[0].escuela != e[1].escuela ]
    misma_escuela = [ e for e in tuplas if e[0].escuela == e[1].escuela ]
    for _tuplas in [distinta_escuela, misma_escuela]:
        while _tuplas:
            tupla = _tuplas.pop()
            if all([not (tupla[0] in encuentro or tupla[1] in encuentro) for encuentro in ronda]):
                ronda.append(tupla)
            if len(ronda) == len(robots) // 2:
                break
    return ronda

GENERADORES = {
    "samu": generador_samu,
    "brutus": generador_brutus,
    "combinaciones": generador_combinaciones
}

class Fixture(object):

    def __init__(self, robots = None):
        self.robots = robots or []
        self.rondas = []
        self._generador = GENERADORES["combinaciones"]

    def inscribir(self, nombre, escuela, responsable):
        robot = Robot(nombre, escuela, responsable)
        self.robots.append(robot)
        return robot

    def crear_ronda(self, tuplas, promovidos):
        encuentros = [Encuentro(*t, numero = i + 1) for i, t in enumerate(tuplas)]
        ronda = Ronda(len(self.rondas) + 1, encuentros, list(promovidos))
        return ronda

    def agregar_ronda(self, ronda):
        self.rondas.append(ronda)

    def generar_ronda(self):
        assert not self.rondas or self.rondas[-1].finalizada(), "No se finalizo la ultima ronda"
        robots = self.robots if not self.rondas else self.rondas[-1].ganadores()
        tuplas = self._generador(robots)
        promovidos = set(robots).difference(set(reduce(lambda a, t: a + t, tuplas, [])))
        ronda = self.crear_ronda(tuplas, promovidos)
        self.agregar_ronda(ronda)
        return ronda

    def limpiar_rondas(self):
        self.rondas = []

    def get_ronda(self, numero):
        return self.rondas[numero - 1]

    # Json dumps and loads
    def to_dict(self):
        return {
            "robots": self.robots,
            "rondas": [ ronda.to_dict() for ronda in self.rondas ]
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, data):
        fixture = cls()
        robots = []
        for robot_data in data["robots"]:
            robot = fixture.inscribir(*robot_data)
            robots.append(robot)
        for ronda_data in data["rondas"]:
            encuentros = []
            for encuentro_data in ronda_data["encuentros"]:
                r1 = [robot for robot in robots if robot == tuple(encuentro_data["robot_1"])].pop()
                r2 = [robot for robot in robots if robot == tuple(encuentro_data["robot_2"])].pop()
                ganadas = [ tuple(gano) == r1 and r1 or r2 for gano in encuentro_data["ganadas"] ]
                encuentro = Encuentro(r1, r2, numero=encuentro_data["numero"], ganadas = ganadas)
                encuentros.append(encuentro)
            promovidos = [robot for robot in robots if robot in [ tuple(p) for p in ronda_data["promovidos"]] ]
            ronda = Ronda(numero=ronda_data["numero"], encuentros = encuentros, promovidos = promovidos)
            fixture.agregar_ronda(ronda)
        return fixture

    def finalizado(self):
        """Un fixture esta finalizado cuando todas las rondas estan finalizadas y la ultima ronda tiene a un solo ganador"""
        tiene_robots = bool(self.robots)
        rondas_finalizadas = bool(self.rondas and all([r.finalizada() for r in self.rondas]))
        ultima_ronda_un_ganador = bool(self.rondas and len(self.rondas[-1].ganadores()) == 1)
        return not tiene_robots or (tiene_robots and rondas_finalizadas and ultima_ronda_un_ganador)

    # Consultas sobre el fixture
    def ganador(self):
        robots = self.robots if not self.rondas else self.rondas[-1].ganadores()
        if robots:
            return robots.pop()

    def score(self, robot):
        """Retorna el *score* de un robot dentro del torneo
        score es una n-upla de la forma (ganadas, perdidas, empates, jugadas, ranking)
        """
        resultados = [ ronda.score(robot) for ronda in self.rondas ]
        print(score)