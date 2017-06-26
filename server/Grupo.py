import random

from .Robot import Robot
from .Ronda import Ronda

class Grupo(object):
    NUMERO = 1
    def __init__(self, robots):
        self.robots = robots
        self.numero = Grupo.NUMERO
        Grupo.NUMERO = Grupo.NUMERO + 1
        self.rondas = []

    @staticmethod
    def generar(robots, numero, esc=True):
        if esc:
            robots = sorted(robots, key=lambda e: e.escuela)
        else:
            robots = robots[:]
            random.shuffle(robots)
        nrobots = len(robots) // numero
        grupos = [robots[n * nrobots:n * nrobots + nrobots] for n in range(numero)]
        for i, r in enumerate(robots[numero*nrobots:], 1):
            index = -(i % len(grupos))
            grupos[index] = grupos[index] + [r]
        return [Grupo(rs) for rs in grupos]

    # Rondas
    def generar_ronda(self, tct=True):
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