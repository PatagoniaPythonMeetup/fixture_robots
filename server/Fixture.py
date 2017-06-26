import random
import json
import sys
from functools import reduce
from itertools import combinations

from .Robot import Robot
from .Encuentro import Encuentro
from .Ronda import Ronda
from .Fase import Clasificacion, Eliminacion, Final

class Fixture(object):
    def __init__(self, robots=None, jugadas=3, tracks=1):
        # Numero de tracks en paralelo que pueden ser sostenidos por disponibilidad de pistas
        Ronda.TRACKS = tracks
        # Numero minimo de jugadas para determinar un ganador en un encuentro
        Encuentro.JUGADAS = jugadas
        self.robots = robots or []
        self.fases = []

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
        ronda_actual = self.get_ronda_actual()
        return self.robots if ronda_actual is None else ronda_actual.get_robots()

    def clasificacion(self, grupos):
        robots = self.robots # O los que vienen de la fase anterior
        clas = Clasificacion(robots, grupos)
        self.fases.append(clas)
        return clas

    def eliminacion(self):
        robots = self.robots # O los que vienen de la fase anterior
        clas = Eliminacion(robots)
        self.fases.append(clas)
        return clas

    def final(self):
        robots = self.robots # O los que vienen de la fase anterior
        clas = Final(robots)
        self.fases.append(clas)
        return clas

    # Encuentros
    def get_encuentros(self):
        return reduce(lambda a, ronda: a + ronda.get_encuentros(), self.get_rondas(), [])

    def get_encuentro(self, numero):
        encuentros = [encuentro for encuentro in self.get_encuentros() \
            if encuentro.numero == numero]
        if len(encuentros) == 1:
            return encuentros.pop()

    def get_encuentros_actuales(self):
        ronda = self.get_ronda_actual()
        return ronda.get_encuentros_actuales() if ronda is not None else []

    # Rondas
    def generar_ronda(self, tct=False, allow_none=False, shuffle=True):
        fase = self.get_fase_actual()
        if fase:
            return fase.generar_ronda(tct, allow_none, shuffle)

    def get_ronda(self, numero):
        rondas = [ronda for ronda in self.get_rondas() if ronda.numero == numero]
        if len(rondas) == 1:
            return rondas.pop()

    def get_rondas(self):
        return reduce(lambda a, fase: a + fase.get_rondas(), self.get_fases(), [])

    def get_ronda_actual(self):
        rondas = self.get_rondas()
        if rondas:
            return rondas[-1]

    # Fases
    def get_fases(self):
        return self.fases[:]

    def get_fase_actual(self):
        fases = self.get_fases()
        if fases:
            return fases[-1]

    # Json dumps and loads
    def to_dict(self):
        return {
            "robots": self.robots,
            "fases": [fase.to_dict() for fase in self.get_fases()]
        }

    def from_dict(self, data):
        robots = []
        for robot_data in data["robots"]:
            robot = self.inscribir_robot(*robot_data)
            robots.append(robot)
        for fase_data in data["fases"]:
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
        tiene_robots = bool(self.robots)
        return tiene_robots and self.get_fase_actual().iniciado()

    def compitiendo(self):
        return self.get_fase_actual().compitiendo()

    def finalizado(self):
        tiene_robots = bool(self.robots)
        return tiene_robots and self.get_fase_actual().finalizado()

    def vuelta(self):
        encuentros = self.get_encuentros()
        return max([e.jugadas() for e in encuentros]) if encuentros else 0
    
    def jugadas(self):
        encuentros = self.get_encuentros()
        return sum([e.jugadas() for e in encuentros]) if encuentros else 0

    # Trabajando sobre el fixture
    def ganadores(self):
        fase = self.get_fase_actual()
        if fase is not None:
            return fase.ganadores()

    def ganador(self):
        ganadores = self.ganadores()
        if len(ganadores) == 1:
            return ganadores[0]

    def score(self, robot):
        """Retorna el *score* de un robot dentro del fixture
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        scores = [ronda.score(robot) for ronda in self.get_rondas()]
        return reduce(lambda acumulador, score: tuple([ a + b for a, b in zip(acumulador, score)]), scores, (0, 0, 0, 0, 0, 0, 0, 0))
        