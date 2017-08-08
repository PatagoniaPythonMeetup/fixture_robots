import random
from functools import reduce

from .Robot import Robot
from .Ronda import Ronda

class Grupo(object):
    NUMERO = 1
    def __init__(self, robots=None, rondas=None):
        self.robots = robots or []
        self.rondas = rondas or []
        self.numero = Grupo.NUMERO
        Grupo.NUMERO = Grupo.NUMERO + 1

    def __len__(self):
        return len(self.robots)
    
    @staticmethod
    def generar(robots, cantidad, esc=True):
        if esc:
            robots = sorted(robots, key=lambda e: e.escuela)
        else:
            robots = robots[:]
            random.shuffle(robots)
        nrobots = len(robots) // cantidad
        grupos = [robots[n * nrobots:n * nrobots + nrobots] for n in range(cantidad)]
        for i, r in enumerate(robots[cantidad*nrobots:], 1):
            index = -(i % len(grupos))
            grupos[index] = grupos[index] + [r]
        return [Grupo(rs) for rs in grupos]

    # Rondas
    def generar_ronda(self, tct=False, allow_none=False, shuffle=True):
        ronda_actual = self.get_ronda_actual()
        assert ronda_actual is None or ronda_actual.finalizado(), "No se finalizo la ultima ronda"
        robots = self.robots if ronda_actual is None else ronda_actual.ganadores()
        assert robots, "No hay robots para participar en una nueva ronda"
        ronda = Ronda.generar(robots, tct, allow_none, shuffle=True)
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
        if rondas:
            return rondas[-1]

    def get_robots(self):
        return self.robots[:]
        
    # Encuentros
    def get_encuentros(self):
        return reduce(lambda a, ronda: a + ronda.encuentros, self.get_rondas(), [])

    def get_encuentro(self, numero):
        encuentros = [encuentro for encuentro in self.get_encuentros() \
            if encuentro.numero == numero]
        if len(encuentros) == 1:
            return encuentros.pop()

    def get_encuentros_actuales(self):
        ronda_actual = self.get_ronda_actual()
        return ronda_actual.get_encuentros_actuales() if ronda_actual is not None else []

    # Estados
    def iniciado(self):
        ronda_actual = self.get_ronda_actual()
        return ronda_actual is not None and ronda_actual.iniciado()

    def compitiendo(self):
        ronda_actual = self.get_ronda_actual()
        return ronda_actual is not None and ronda_actual.compitiendo()

    def finalizado(self):
        ronda_actual = self.get_ronda_actual()
        return ronda_actual is not None and ronda_actual.finalizado()

    def jugadas(self):
        encuentros = self.get_encuentros()
        return sum([e.jugadas() for e in encuentros]) if encuentros else 0

    # Serialize
    def to_dict(self):
        return {
            "robots": self.robots,
            "rondas": [ronda.to_dict() for ronda in self.get_rondas()]
        }

    def ganador(self):
        ronda_actual = self.get_ronda_actual()
        if ronda_actual:
            return ronda_actual.ganador()

    def ganadores(self):
        ronda_actual = self.get_ronda_actual()
        if ronda_actual:
            return ronda_actual.ganadores()
        return []

    def perdedor(self):
        ronda_actual = self.get_ronda_actual()
        if ronda_actual:
            return ronda_actual.perdedor()

    def perdedores(self):
        ronda_actual = self.get_ronda_actual()
        if ronda_actual:
            return ronda_actual.perdedores()
        return []
    
    # Score en el grupo
    def score(self, robot):
        """Retorna el *score* de un robot dentro del grupo
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        scores = [ronda.score(robot) for ronda in self.get_rondas()]
        return reduce(lambda acumulador, score: tuple([ a + b for a, b in zip(acumulador, score)]), scores, (0, 0, 0, 0, 0, 0, 0, 0))