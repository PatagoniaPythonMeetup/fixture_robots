from functools import reduce
from .Grupo import Grupo

class Fase(object):
    NUMERO = 1

    def __init__(self, robots, grupos=None):
        self.numero = Fase.NUMERO
        Fase.NUMERO = Fase.NUMERO + 1
        self.robots = robots
        self.grupos = grupos or []

    def get_nombre(self):
        return self.__class__.__name__
    
    def get_grupos(self):
        return self.grupos[:]

    def get_encuentros(self):
        return reduce(lambda a, ronda: a + ronda.get_encuentros(), self.get_rondas(), [])

    def get_rondas(self):
        return reduce(lambda a, grupo: a + grupo.get_rondas(), self.get_grupos(), [])

    def get_rondas_actuales(self):
        rondas = []
        for grupo in self.get_grupos():
            rondas_del_grupo = grupo.get_rondas()
            if rondas_del_grupo:
                rondas.append(rondas_del_grupo[-1])
        return rondas

    def generar_rondas(self, tct=False, allow_none=False, shuffle=True):
        return [grupo.generar_ronda(tct, allow_none, shuffle) for grupo in self.get_grupos()]

    def get_robots(self):
        return reduce(lambda a, grupo: a + grupo.get_robots(), self.get_grupos(), [])

    # Estados
    def iniciado(self):
        rondas_actuales = self.get_rondas_actuales()
        return rondas_actuales and \
        any([ronda_actual.iniciado() for ronda_actual in rondas_actuales])

    def compitiendo(self):
        rondas_actuales = self.get_rondas_actuales()
        return rondas_actuales and \
        any([ronda_actual.compitiendo() for ronda_actual in rondas_actuales])

    def finalizado(self):
        rondas_actuales = self.get_rondas_actuales()
        return rondas_actuales and \
        all([ronda_actual.finalizado() for ronda_actual in rondas_actuales])

    def ganadores(self):
        return reduce(lambda a, grupo: a + grupo.ganadores(), self.get_grupos(), [])

    def perdedores(self):
        return reduce(lambda a, grupo: a + grupo.perdedores(), self.get_grupos(), [])

    # Serialize
    def to_dict(self):
        return {
            "nombre": self.get_nombre(),
            "grupos": [grupo.to_dict() for grupo in self.get_grupos()]
        }

    # Trabajando sobre la fase
    def participa(self, robot):
        return any([g.participa(robot) for g in self.get_grupos()])

    def score(self, robot):
        """Retorna el *score* de un robot dentro de la fase
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        scores = [grupo.score(robot) for grupo in self.get_grupos()]
        return reduce(lambda acumulador, score: tuple([ a + b for a, b in zip(acumulador, score)]), scores, (0, 0, 0, 0, 0, 0, 0, 0))

class Clasificacion(Fase):
    """Fase en la que los robots son separados en N grupos de donde se tomaran solo a los mas sobresalientes"""
    def __init__(self, robots, grupos=None):
        if isinstance(grupos, int):
            grupos = Grupo.generar(robots, grupos)
        super().__init__(robots, grupos)

class Eliminacion(Fase):
    """Fase con un solo grupo donde todos compiten contra todos"""
    def __init__(self, robots, grupos=None):
        if grupos is None:
            grupos = [Grupo(robots)]
        super().__init__(robots, grupos)

class Final(Fase):
    """Fase donde los robots son separados en dos grupos y se enfrentan hasta quedar dos en la final"""
    NOMBRES = {
        16: "Octavos",
        8: "Cuartos",
        4: "Semifinal",
        2: "Final"
    }

    def __init__(self, robots, grupos=None):
        assert len(robots) in self.NOMBRES, "El numero de para una final debe ser 16, 8, 4 o 2"
        if grupos is None:
            n = len(robots) // 2
            grupos = [Grupo(robots[:n]), Grupo(robots[n:])]
        super().__init__(robots, grupos)

    def posiciones(self):
        scores = [(r,) + self.score(r) for r in self.get_robots()]
        return sorted(scores, key=lambda s: s[8], reverse=True)