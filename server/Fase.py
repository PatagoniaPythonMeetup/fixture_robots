from functools import reduce
from .Grupo import Grupo

class Fase(object):
    def __init__(self, grupos):
        self.grupos = grupos or []

    def get_grupos(self):
        return self.grupos[:]

    def get_encuentros(self):
        return reduce(lambda a, ronda: a + ronda.get_encuentros(), self.get_rondas(), [])

    def get_rondas(self):
        return reduce(lambda a, grupo: a + grupo.get_rondas(), self.get_grupos(), [])

    def get_ronda_actual(self):
        rondas = self.get_rondas()
        if rondas:
            return rondas[-1]

    def generar_rondas(self, tct=False, allow_none=False, shuffle=True):
        return [grupo.generar_ronda(tct, allow_none, shuffle) for grupo in self.get_grupos()]

    def get_robots(self):
        return reduce(lambda a, grupo: a + grupo.get_robots(), self.get_grupos(), [])

    # Estados
    def iniciado(self):
        ronda_actual = self.get_ronda_actual()
        return ronda_actual is not None and ronda_actual.iniciado() and ronda_actual.ganador() is None

    def compitiendo(self):
        ronda_actual = self.get_ronda_actual()
        return ronda_actual is not None and ronda_actual.compitiendo()

    def finalizado(self):
        ronda_actual = self.get_ronda_actual()
        return ronda_actual is not None and ronda_actual.finalizado() and ronda_actual.ganador()

    def ganadores(self):
        return reduce(lambda a, grupo: a + grupo.ganadores(), self.get_grupos(), [])

    def perdedores(self):
        return reduce(lambda a, grupo: a + grupo.perdedores(), self.get_grupos(), [])

    # Serialize
    def to_dict(self):
        return {
            "grupos": [grupo.to_dict() for grupo in self.get_grupos()]
        }

    def score(self, robot):
        """Retorna el *score* de un robot dentro de la fase
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        scores = [grupo.score(robot) for grupo in self.get_grupos()]
        return reduce(lambda acumulador, score: tuple([ a + b for a, b in zip(acumulador, score)]), scores, (0, 0, 0, 0, 0, 0, 0, 0))

class Clasificacion(Fase):
    """Fase en la que los robots son separados en N grupos de donde se tomaran solo a los mas sobresalientes"""
    def __init__(self, robots, grupos):
        super().__init__(Grupo.generar(robots, grupos))

class Eliminacion(Fase):
    """Fase con un solo grupo donde todos compiten contra todos"""
    def __init__(self, robots):
        super().__init__([Grupo(robots)])

class Final(Fase):
    """Fase donde los robots son separados en dos grupos y se enfrentan hasta quedar dos en la final"""
    def __init__(self, robots):
        super().__init__([Grupo(robots)])

    def posiciones(self):
        scores = [(r,) + self.score(r) for r in self.get_robots()]
        return sorted(scores, key=lambda s: s[8], reverse=True)