from functools import reduce

from .Robot import Robot

class Ronda(object):
    def __init__(self, numero, encuentros, promovidos=None, tct=False):
        self.numero = numero
        self.encuentros = encuentros
        self.promovidos = promovidos or []
        self.tct = tct

    @property
    def robots(self):
        return list(reduce(lambda a, e: a.union([e.robot_1, e.robot_2]), self.encuentros, set(self.promovidos)))

    def participa(self, robot):
        return robot in self.promovidos or any([e.participa(robot) for e in self.encuentros])

    def finalizada(self):
        return all([e.finalizado() for e in self.encuentros])

    def ganadores(self):
        if self.tct:
            scores = [(r,) + self.score(r) for r in self.robots]
            scores = sorted(scores, key=lambda s: s[6], reverse=True)
            #TODO: Mejorar como se obtiene este ganador de un tct
            return [scores[0][0]]
        else:
            return [e.ganador() for e in self.encuentros] + self.promovidos

    def ganador(self):
        ganadores = self.ganadores()
        if len(ganadores) == 1:
            return ganadores.pop()

    def get_encuentro(self, numero):
        encuentros = [encuentro for encuentro in self.encuentros if encuentro.numero == numero]
        if encuentros:
            return encuentros.pop()
    
    def gano(self, robot, encuentro=None):
        encuentros = [e for e in self.encuentros if e.participa(robot) and (encuentro is None or (encuentro is not None and e.numero == encuentro))]
        assert len(encuentros) == 1, "El robot no participa de la ronda o debe especificar un encuentro"
        encuentros[0].gano(robot)

    def vuelta(self):
        return max([e.jugadas() for e in self.encuentros])
    
    def jugadas(self):
        return sum([e.jugadas() for e in self.encuentros])

    def score(self, robot):
        """Retorna el *score* de un robot dentro de la ronda
        score es una n-upla de la forma (jugado, victorias, derrotas, empates, diferencia, puntos)
        """
        resultados = [encuentro.score(robot) for encuentro in self.encuentros if encuentro.participa(robot)]
        victorias = len([resultado for resultado in resultados if None not in resultado and resultado[0] > resultado[1]])
        derrotas = len([resultado for resultado in resultados if None not in resultado and resultado[0] < resultado[1]])
        empates = len([resultado for resultado in resultados if None not in resultado and resultado[0] == resultado[1]])
        puntos = victorias * 3 + empates * 1 + derrotas * 0
        diferencia = reduce(lambda acumulador, resultado: acumulador + resultado[0] - resultado[1], [resultado for resultado in resultados if None not in resultado], 0)
        return (victorias + derrotas + empates, victorias, derrotas, empates, diferencia, puntos)

    def to_dict(self):
        return {
            "numero": self.numero,
            "encuentros": [ encuentro.to_dict() for encuentro in self.encuentros ],
            "promovidos": self.promovidos,
            "tct": self.tct
        }
