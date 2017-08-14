import random
import json
import sys
from functools import reduce
from itertools import combinations

from .Robot import Robot
from .Encuentro import Encuentro
from .Ronda import Ronda
from .Grupo import Grupo
from .Fase import Clasificacion, Eliminacion, Final, AdHoc

class Fixture(object):
    def __init__(self, equipos=None, robots=None, jugadas=3, tracks=1):
        # Numero de tracks en paralelo que pueden ser sostenidos por disponibilidad de pistas
        Ronda.TRACKS = tracks
        # Numero minimo de jugadas para determinar un ganador en un encuentro
        Encuentro.JUGADAS = jugadas
        self.equipos = equipos or []
        self.robots = robots or []
        self.fases = []

    # Equipos
    def inscribir_equipo(self, equipo):
        robot = equipo.robot
        self.robots.append(robot)
        self.equipos.append(equipo)
        return robot

    # Robots
    def inscribir_robot(self, nombre, escuela, responsable, escudo=None):
        robot = Robot(nombre, escuela, responsable, escudo)
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

    def clasificacion(self, grupos, esc):
        assert grupos is not None, "Debe indicar el numero de grupos para la fase de clasificacion"
        fase_actual = self.get_fase_actual()
        assert fase_actual is None or fase_actual.finalizado(), "La fase actual no fue finalizada"
        robots = fase_actual.ganadores() if fase_actual is not None else self.get_robots()
        grupos = Grupo.generar(robots, grupos, esc)
        clas = Clasificacion(robots, grupos)
        self.fases.append(clas)
        return clas

    def eliminacion(self):
        fase_actual = self.get_fase_actual()
        assert fase_actual is None or fase_actual.finalizado(), "La fase actual no fue finalizada"
        robots = fase_actual.ganadores() if fase_actual is not None else self.get_robots()
        grupos = [Grupo(robots)]
        clas = Eliminacion(robots, grupos)
        self.fases.append(clas)
        return clas

    def final(self, jugadores):
        assert jugadores in Final.NOMBRES, "El numero de para una final debe ser 16, 8, 4 o 2"
        fase_actual = self.get_fase_actual()
        assert fase_actual is None or fase_actual.finalizado(), "La fase actual no fue finalizada"
        #TODO: Algo importante es que si estan ordenados por puntos los mejors se enfrentan seguro si no se hace un shuffle
        robots = fase_actual.ganadores() if fase_actual is not None else self.get_robots()
        robots = robots[:jugadores]
        mitad = len(robots) // 2
        nombre = Final.NOMBRES[len(robots)]
        grupos = [Grupo(robots=robots[:mitad], nombre=nombre), Grupo(robots=robots[mitad:], nombre=nombre)]
        clas = Final(robots, grupos)
        self.fases.append(clas)
        return clas

    def adhoc(self, robots):
        fase_actual = self.get_fase_actual()
        assert fase_actual is None or fase_actual.finalizado(), "La fase actual no fue finalizada"
        robots = [robot for robot in self.get_robots() if robot.key in robots]
        grupos = [Grupo(robots)]
        clas = AdHoc(robots, grupos)
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

    def agregar_adversario(self, numero):
        """Busca un encuentro dentro de una ronda y si no es valido lo resuleve 
        usando los perdedores de la ronda.
        Resuelve solo cuando es el ultimo encuentro que queda por finalizar"""
        for ronda in self.get_rondas():
            encuentros = [encuentro for encuentro in ronda.get_encuentros() if encuentro.numero == numero]
            if encuentros:
                assert all([e.finalizado() for e in ronda.get_encuentros() if e.numero != numero]), "Debe finalizar todos los encuentros previos en la ronda" 
                encuentros[0].agregar_adversario(random.choice(ronda.perdedores()))
                return encuentros[0]

    def armar_final(self, numero):
        """Busca un fase final y loa completa con los robots de la fase
        Completa solo cuando el resto de la fase esta finalizada"""
        fases =[fase for fase in self.get_fases() if fase.numero == numero]
        if fases:
            fase = fases.pop()
            if isinstance(fase, Final):
                fase.completar()
                return fase

    # Rondas
    def generar_ronda(self, ngrupo, tct, esc, allow_none, shuffle):
        fase = self.get_fase_actual()
        if fase:
            return fase.generar_ronda(ngrupo, tct, esc, allow_none, shuffle)

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
    def get_fase(self, numero):
        fases = [fase for fase in self.get_fases() if fase.numero == numero]
        if len(fases) == 1:
            return fases.pop()

    def get_fases(self):
        return self.fases[:]

    def get_fase_actual(self):
        fases = self.get_fases()
        if fases:
            return fases[-1]

    def limpiar(self):
        self.robots = []
        self.fases = []

    # Json dumps and loads
    def to_dict(self):
        return {
            "robots": self.robots,
            "fases": [fase.to_dict() for fase in self.get_fases()]
        }

    def from_dict(self, data):
        CLASES = {kls.__name__: kls for kls in [Clasificacion, Eliminacion, Final]}
        robots = [Robot(*robot_data) for robot_data in data["robots"]]
        fases = []
        for fase_data in data["fases"]:
            klass = fase_data["nombre"]
            grupos = []
            frobots = []
            for grupo_data in fase_data["grupos"]:
                rondas = []
                for ronda_data in grupo_data["rondas"]:
                    encuentros = []
                    for encuentro_data in ronda_data["encuentros"]:
                        r1 = Robot(*encuentro_data["robot_1"])
                        r2 = Robot(*encuentro_data["robot_2"])
                        ganadas = [Robot(*gano) == r1 and r1 or r2 for gano in encuentro_data["ganadas"]]
                        encuentro = Encuentro(r1, r2, ganadas=ganadas)
                        encuentros.append(encuentro)
                    promovidos = [robot for robot in robots \
                        if robot in [Robot(*p) for p in ronda_data["promovidos"]]]
                    rondas.append(Ronda(encuentros=encuentros, \
                        promovidos=promovidos, tct=ronda_data.pop("tct", False), nombre=grupo_data.pop("nombre")))
                grobots = [robot for robot in robots \
                    if robot in [Robot(*p) for p in grupo_data["robots"]]]
                frobots = frobots + grobots
                grupos.append(Grupo(robots=grobots, rondas=rondas, nombre=grupo_data.pop("nombre")))
            fases.append(CLASES[klass](frobots, grupos))
        self.robots = robots
        self.fases = fases

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
        fase_actual = self.get_fase_actual()
        return tiene_robots and fase_actual is not None

    def compitiendo(self):
        fase_actual = self.get_fase_actual()
        return fase_actual is not None and (fase_actual.compitiendo() or not fase_actual.iniciado())

    def finalizado(self):
        tiene_robots = bool(self.robots)
        tiene_ganador = bool(self.ganador())
        fase_actual = self.get_fase_actual()
        return tiene_robots and tiene_ganador and fase_actual and fase_actual.finalizado()

    def jugadas(self):
        encuentros = self.get_encuentros()
        return sum([e.jugadas() for e in encuentros]) if encuentros else 0

    # Trabajando sobre el fixture
    def ganadores(self):
        fase = self.get_fase_actual()
        if fase is not None:
            return fase.ganadores()

    def ganador(self):
        fase = self.get_fase_actual()
        if fase is not None:
            return fase.ganador()
    
    def perdedores(self):
        fase = self.get_fase_actual()
        if fase is not None:
            return fase.perdedores()

    def perdedor(self):
        fase = self.get_fase_actual()
        if fase is not None:
            return fase.perdedor()

    def agregar_ganador(self, robot, nencuentro=None):
        encuentros = [e for e in self.get_encuentros() if e.participa(robot) and (nencuentro is None or (nencuentro is not None and e.numero == nencuentro))]
        assert len(encuentros) == 1, "El robot no participa de la ronda o debe especificar un encuentro"
        encuentro = encuentros[0]
        encuentro.agregar_ganador(robot)
        return encuentro

    def quitar_ganador(self, robot, nencuentro=None):
        encuentros = [e for e in self.get_encuentros() if e.participa(robot) and (nencuentro is None or (nencuentro is not None and e.numero == nencuentro))]
        assert len(encuentros) == 1, "El robot no participa de la ronda o debe especificar un encuentro"
        encuentro = encuentros[0]
        encuentro.quitar_ganador(robot)
        return encuentro

    def score(self, robot):
        """Retorna el *score* de un robot dentro del fixture
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        scores = [ronda.score(robot) for ronda in self.get_rondas()]
        return reduce(lambda acumulador, score: tuple([ a + b for a, b in zip(acumulador, score)]), scores, (0, 0, 0, 0, 0, 0, 0, 0))
        