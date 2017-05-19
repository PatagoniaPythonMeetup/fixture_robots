from functools import reduce

from .Robot import Robot

class Ronda(object):
    TRACKS_EN_PARALELO = 1
    def __init__(self, numero, encuentros, promovidos=None, tct=False):
        self.numero = numero
        self.encuentros = encuentros
        self.promovidos = promovidos or []
        self.tct = tct

    # Robots
    @property
    def robots(self):
        return list(reduce(lambda a, e: a.union([e.robot_1, e.robot_2]), self.encuentros, set(self.promovidos)))

    def ganadores(self):
        if self.tct:
            scores = [(r,) + self.score(r) for r in self.robots]
            scores = sorted(scores, key=lambda s: s[8], reverse=True)
            # El mejor puntuado es el ganador de esta ronda de todos contra todos
            return [scores[0][0]]
        else:
            return [e.ganador() for e in self.encuentros] + self.promovidos

    def ganador(self):
        ganadores = self.ganadores()
        if self.finalizado() and len(ganadores) == 1:
            return ganadores.pop()

    # Encuentros
    def get_encuentro(self, numero):
        encuentros = [encuentro for encuentro in self.encuentros if encuentro.numero == numero]
        if encuentros:
            return encuentros.pop()

    def get_encuentros_actuales(self):
        encuentros = [encuentro for encuentro in self.encuentros if not encuentro.finalizado()]
        return encuentros[:self.TRACKS_EN_PARALELO]

    # Json dumps and loads
    def to_dict(self):
        return {
            "numero": self.numero,
            "encuentros": [ encuentro.to_dict() for encuentro in self.encuentros ],
            "promovidos": self.promovidos,
            "tct": self.tct
        }

    # Estados
    def iniciado(self):
        return not self.finalizado()

    def finalizado(self):
        return all([e.finalizado() for e in self.encuentros])
    
    def compitiendo(self):
        return not self.finalizado()

    def vuelta(self):
        return max([e.jugadas() for e in self.encuentros])
    
    def jugadas(self):
        return sum([e.jugadas() for e in self.encuentros])

    # Trabajando sobre la ronda
    def participa(self, robot):
        return robot in self.promovidos or any([e.participa(robot) for e in self.encuentros])

    def gano(self, robot, nencuentro=None):
        encuentros = [e for e in self.encuentros if e.participa(robot) and (nencuentro is None or (nencuentro is not None and e.numero == nencuentro))]
        assert len(encuentros) == 1, "El robot no participa de la ronda o debe especificar un encuentro"
        encuentro = encuentros[0]
        encuentro.gano(robot)
        return encuentro

    def score(self, robot):
        """Retorna el *score* de un robot dentro de la ronda
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        resultados = [encuentro.score(robot) for encuentro in self.encuentros if encuentro.participa(robot)]
        resultados = [resultado for resultado in resultados if None not in resultado ]
        triunfos = len([resultado for resultado in resultados if resultado[0] > resultado[1]])
        derrotas = len([resultado for resultado in resultados if resultado[0] < resultado[1]])
        empates = len([resultado for resultado in resultados if resultado[0] == resultado[1]])
        puntos = triunfos * 3 + empates * 1 + derrotas * 0
        a_favor = reduce(lambda acumulador, resultado: acumulador + resultado[0], resultados, 0)
        en_contra = reduce(lambda acumulador, resultado: acumulador + resultado[1], resultados, 0)
        return (triunfos + derrotas + empates, triunfos, empates, derrotas, a_favor, en_contra, a_favor - en_contra, puntos)
