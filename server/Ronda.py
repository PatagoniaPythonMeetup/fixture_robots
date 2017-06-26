import random
from functools import reduce
from itertools import combinations

from .Robot import Robot
from .Encuentro import Encuentro

class Ronda(object):
    TRACKS = 1
    NUMERO = 1
    def __init__(self, encuentros, promovidos=None, tct=False):
        self.numero = Ronda.NUMERO
        Ronda.NUMERO = Ronda.NUMERO + 1
        self.encuentros = encuentros
        self.promovidos = promovidos or []
        self.tct = tct

    #Generar nueva ronda
    @staticmethod
    def generar(robots, tct=False, allow_none=False, shuffle=True):
        tuplas = [list(combine) for combine in combinations(robots, 2)]
        ronda_tuplas = []
        if shuffle:
            random.shuffle(tuplas)
        distinta_escuela = [e for e in tuplas if e[0].escuela != e[1].escuela]
        misma_escuela = [e for e in tuplas if e[0].escuela == e[1].escuela]
        for _tuplas in [distinta_escuela, misma_escuela]:
            while _tuplas:
                tupla = _tuplas.pop()
                if tct or all([not (tupla[0] in encuentro or tupla[1] in encuentro) for encuentro in ronda_tuplas]):
                    ronda_tuplas.append(tupla)
                if not tct and len(ronda_tuplas) == len(robots) // 2:
                    break
        # Ahora creamos la ronda
        promovidos = set(robots).difference(set(reduce(lambda a, t: a + t, ronda_tuplas, [])))
        if promovidos and allow_none:
            for t in [(p, None) for p in promovidos]:
                ronda_tuplas.append(t)
            promovidos = []
        encuentros = [Encuentro(*t) for t in ronda_tuplas]
        return Ronda(encuentros, list(promovidos), tct)

    # Robots
    def get_robots(self):
        return list(reduce(lambda a, e: a.union([e.robot_1, e.robot_2]), self.encuentros, set(self.promovidos)))

    def ganadores(self):
        if self.tct:
            scores = [(r,) + self.score(r) for r in self.get_robots()]
            scores = sorted(scores, key=lambda s: s[8], reverse=True)
            return [s[0] for s in scores] + self.promovidos
        else:
            return [e.ganador() for e in self.encuentros] + self.promovidos

    def ganador(self):
        ganadores = self.ganadores()
        if self.finalizado() and len(ganadores) == 1 or self.tct:
            return ganadores[0]

    # Encuentros
    def get_encuentros(self):
        return self.encuentros[:]
        
    def get_encuentro(self, numero):
        encuentros = [encuentro for encuentro in self.get_encuentros() if encuentro.numero == numero]
        if encuentros:
            return encuentros.pop()

    def get_encuentros_actuales(self):
        encuentros = [encuentro for encuentro in self.get_encuentros() if not encuentro.finalizado()]
        return encuentros[:self.TRACKS]

    # Json dumps and loads
    def to_dict(self):
        return {
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
        encuentros = [encuentro for encuentro in self.encuentros if encuentro.finalizado()]
        resultados = [encuentro.score(robot) for encuentro in encuentros if encuentro.participa(robot)]
        resultados = [resultado for resultado in resultados if None not in resultado ]
        triunfos = len([resultado for resultado in resultados if resultado[0] > resultado[1]])
        derrotas = len([resultado for resultado in resultados if resultado[0] < resultado[1]])
        empates = len([resultado for resultado in resultados if resultado[0] == resultado[1]])
        puntos = triunfos * 3 + empates * 1 + derrotas * 0
        a_favor = reduce(lambda acumulador, resultado: acumulador + resultado[0], resultados, 0)
        en_contra = reduce(lambda acumulador, resultado: acumulador + resultado[1], resultados, 0)
        return (triunfos + derrotas + empates, triunfos, empates, derrotas, a_favor, en_contra, a_favor - en_contra, puntos)
