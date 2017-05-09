import random
import json
from functools import reduce
from itertools import combinations

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

def generador_combinaciones(robots, tct):
    tuplas = [list(combine) for combine in combinations(robots, 2)]
    ronda = []
    random.shuffle(tuplas)
    distinta_escuela = [ e for e in tuplas if e[0].escuela != e[1].escuela ]
    misma_escuela = [ e for e in tuplas if e[0].escuela == e[1].escuela ]
    for _tuplas in [distinta_escuela, misma_escuela]:
        while _tuplas:
            tupla = _tuplas.pop()
            if tct or all([not (tupla[0] in encuentro or tupla[1] in encuentro) for encuentro in ronda]):
                ronda.append(tupla)
            if not tct and len(ronda) == len(robots) // 2:
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
    
    # Robots
    def inscribir_robot(self, nombre, escuela, responsable):
        robot = Robot(nombre, escuela, responsable)
        self.robots.append(robot)
        return robot

    def get_robot_por_nombre(self, nombre):
        robots = [robot for robot in self.robots if robot.nombre == nombre]
        if len(robots) == 1:
            return robots.pop()

    def get_robot_por_key(self, key):
        robots = [robot for robot in self.robots if robot.key == key]
        if len(robots) == 1:
            return robots.pop()

    def robots_en_juego(self):
        ronda = self.get_ronda_actual()
        return self.robots if not ronda else ronda.robots
    
    # Rondas
    def crear_ronda(self, tuplas, promovidos, tct):
        encuentros = [Encuentro(*t, numero = i + 1) for i, t in enumerate(tuplas)]
        ronda = Ronda(len(self.rondas) + 1, encuentros, list(promovidos), tct)
        return ronda

    def agregar_ronda(self, ronda):
        self.rondas.append(ronda)

    def generar_ronda(self, tct=False):
        assert not self.rondas or self.rondas[-1].finalizada(), "No se finalizo la ultima ronda"
        robots = self.robots if not self.rondas else self.rondas[-1].ganadores()
        tuplas = self._generador(robots, tct)
        promovidos = set(robots).difference(set(reduce(lambda a, t: a + t, tuplas, [])))
        ronda = self.crear_ronda(tuplas, promovidos, tct=tct)
        self.agregar_ronda(ronda)
        return ronda

    def get_ronda(self, numero):
        rondas = [ronda for ronda in self.rondas if ronda.numero == numero]
        if len(rondas) == 1:
            return rondas.pop()
    
    def get_ronda_actual(self):
        if self.rondas and not self.finalizado():
            return self.rondas[-1]

    # Encuentros
    def get_encuentros_actuales(self):
        ronda = self.get_ronda_actual()
        if ronda is not None:
            return ronda.get_encuentros_actuales()

    # Limpiar
    def limpiar_rondas(self):
        self.rondas = []

    def limpiar_robots(self):
        self.robots = []

    def limpiar(self):
        self.limpiar_robots()
        self.limpiar_rondas()

    # Json dumps and loads
    def to_dict(self):
        return {
            "robots": self.robots,
            "rondas": [ ronda.to_dict() for ronda in self.rondas ]
        }

    def from_dict(self, data):
        self.limpiar()
        robots = []
        for robot_data in data["robots"]:
            robot = self.inscribir_robot(*robot_data)
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
            ronda = Ronda(numero=ronda_data["numero"], encuentros = encuentros, promovidos = promovidos, tct = ronda_data.pop("tct", False))
            self.agregar_ronda(ronda)

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, source):
        fixture = cls()
        fixture.from_dict(json.loads(source))
        return fixture

    # Estados
    def iniciado(self):
        tiene_robots = bool(self.robots)
        tiene_rondas = bool(self.rondas)
        tiene_ganador = bool(self.ganador())
        return tiene_robots and tiene_rondas and not tiene_ganador

    def finalizado(self):
        tiene_robots = bool(self.robots)
        tiene_rondas = bool(self.rondas)
        tiene_ganador = bool(self.ganador())
        return (tiene_robots and tiene_rondas and tiene_ganador) or (not tiene_robots)

    # Trabajando sobre el fixture
    def ganador(self):
        if self.rondas:
            robots = self.rondas[-1].ganadores()
            if len(robots) == 1:
                return robots.pop()

    def gano(self, robot, ronda=None, encuentro=None):
        ronda = self.get_ronda_actual() if ronda is None else self.get_ronda(ronda)
        assert ronda is not None, "No hay ronda actual o el numero de ronda no es correcto"
        assert ronda.participa(robot), "El robot no participa de la ronda"
        ronda.gano(robot, encuentro=encuentro)

    def score(self, robot):
        """Retorna el *score* de un robot dentro del torneo
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        scores = [ronda.score(robot) for ronda in self.rondas]
        return reduce(lambda acumulador, score: tuple([ a + b for a, b in zip(acumulador, score)]), scores, (0, 0, 0, 0, 0, 0, 0, 0))
        