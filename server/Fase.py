from functools import reduce
from .Grupo import Grupo

class Fase(object):
    def __init__(self, grupos):
        self.grupos = grupos or []

    def get_rondas(self):
        return reduce(lambda a, grupo: a + grupo.get_rondas(), self.grupos, [])

    def get_ronda_actual(self):
        rondas = self.get_rondas()
        if rondas:
            return rondas[-1]

    def generar_ronda(self, tct=False, allow_none=False, shuffle=True):
        return [grupo.generar_ronda(tct, allow_none, shuffle) for grupo in self.groups]

    # Estados
    def iniciado(self):
        rondas = self.get_rondas()
        tiene_rondas = bool(rondas)
        tiene_ganadores = bool(self.ganadores())
        return tiene_rondas and not tiene_ganadores

    def compitiendo(self):
        ronda_actual = self.get_ronda_actual()
        return ronda_actual is not None and ronda_actual.compitiendo()

    def finalizado(self):
        rondas = self.get_rondas()
        tiene_rondas = bool(rondas)
        tiene_ganadores = bool(self.ganadores())
        rondas_finalizadas = all([ronda.finalizado() for ronda in rondas])
        return tiene_rondas and rondas_finalizadas and tiene_ganadores

class Clasificacion(Fase):
    def __init__(self, robots, grupos):
        super().__init__(Grupo.generar(robots, grupos))

class Eliminacion(Fase):
    def __init__(self, robots):
        super().__init__([Grupo(robots)])

class Final(Fase):
    def __init__(self, robots):
        super().__init__([Grupo(robots)])
