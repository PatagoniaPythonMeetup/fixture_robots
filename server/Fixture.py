import random
import json
import sys
from functools import reduce
from itertools import combinations

from .Robot import Robot
from .Encuentro import Encuentro
from .Ronda import Ronda

class Fixture(object):
    def __init__(self, robots=None):
        self.robots = robots or []
        self.fases = []
        self.rondas = []

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

    def get_robots(self):
        return self.robots[:]

    def robots_en_juego(self):
        ronda = self.get_ronda_actual()
        return self.robots if not ronda else ronda.robots

    # Encuentros
    def get_encuentros(self):
        return reduce(lambda a, ronda: a + ronda.encuentros, self.get_rondas(), [])

    def get_encuentro(self, numero):
        encuentros = [encuentro for encuentro in self.get_encuentros() \
            if encuentro.numero == numero]
        if len(encuentros) == 1:
            return encuentros.pop()

    def get_encuentros_actuales(self):
        ronda = self.get_ronda_actual()
        return ronda.get_encuentros_actuales() if ronda is not None else []

    # Rondas
    def generar_ronda(self, tct=False):
        ronda_actual = self.get_ronda_actual()
        assert ronda_actual is None or ronda_actual.finalizado(), "No se finalizo la ultima ronda"
        robots = self.robots if ronda_actual is None else ronda_actual.ganadores()
        assert robots, "No hay robots para participar en una nueva ronda"
        ronda = Ronda.generar(robots, tct)
        self.rondas.append(ronda)
        return ronda

    def get_ronda(self, numero):
        rondas = [ronda for ronda in self.get_rondas() if ronda.numero == numero]
        if len(rondas) == 1:
            return rondas.pop()

    def get_rondas(self):
        return self.rondas[:]

    def get_ronda_actual(self):
        rondas = self.get_rondas()
        if rondas and not self.finalizado():
            return rondas[-1]

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
            "rondas": [ronda.to_dict() for ronda in self.get_rondas()]
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
                ganadas = [tuple(gano) == r1 and r1 or r2 for gano in encuentro_data["ganadas"]]
                encuentro = Encuentro(r1, r2, numero=encuentro_data["numero"], ganadas=ganadas)
                encuentros.append(encuentro)
            promovidos = [robot for robot in robots \
                if robot in [tuple(p) for p in ronda_data["promovidos"]]]
            ronda = Ronda(numero=ronda_data["numero"], encuentros=encuentros, \
                promovidos=promovidos, tct=ronda_data.pop("tct", False))
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
        rondas = self.get_rondas()
        tiene_robots = bool(self.robots)
        tiene_rondas = bool(rondas)
        tiene_ganador = bool(self.ganador())
        return tiene_robots and tiene_rondas and not tiene_ganador

    def compitiendo(self):
        ronda = self.get_ronda_actual()
        return ronda is not None and ronda.compitiendo()

    def finalizado(self):
        rondas = self.get_rondas()
        tiene_robots = bool(self.robots)
        tiene_rondas = bool(rondas)
        tiene_ganador = bool(self.ganador())
        rondas_finalizadas = all([ronda.finalizado() for ronda in rondas])
        return (tiene_robots and tiene_rondas and rondas_finalizadas and tiene_ganador) or (not tiene_robots)

    def vuelta(self):
        encuentros = self.get_encuentros()
        return max([e.jugadas() for e in encuentros]) if encuentros else 0
    
    def jugadas(self):
        encuentros = self.get_encuentros()
        return sum([e.jugadas() for e in encuentros]) if encuentros else 0

    # Trabajando sobre el fixture
    def ganador(self):
        rondas = self.get_rondas()
        if rondas:
            robots = rondas[-1].ganadores()
            if len(robots) == 1:
                return robots.pop()

    # TODO: La verdad que se podria hacer que en funcion del estado del encuentro 
    # se obtenga cual es el que corresponde al robot y si el robot no esta en ese encuentro 
    # fallar. La forma en que funciona hoy el metodo permite que puedas hacer ganar a un 
    # robot aunque no sea parte del encuentro en curso, sera util?
    def gano(self, robot, nencuentro=None):
        encuentros = [e for e in self.get_encuentros() if e.participa(robot)]
        if nencuentro is not None:
            encuentros = [e for e in encuentros if e.numero == nencuentro]
        assert len(encuentros) == 1, "El robot no participa de la ronda o debe especificar un encuentro"
        encuentro = encuentros[0]
        encuentro.gano(robot)
        return encuentro

    def score(self, robot):
        """Retorna el *score* de un robot dentro del torneo
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        scores = [ronda.score(robot) for ronda in self.get_rondas()]
        return reduce(lambda acumulador, score: tuple([ a + b for a, b in zip(acumulador, score)]), scores, (0, 0, 0, 0, 0, 0, 0, 0))
        