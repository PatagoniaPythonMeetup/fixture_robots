import random
from functools import reduce
from itertools import combinations

from .Robot import Robot
from .Encuentro import Encuentro

class Ronda(object):
    TRACKS = 1
    NUMERO = 1
    def __init__(self, encuentros, promovidos=None, tct=False, nombre=None):
        self.numero = Ronda.NUMERO
        Ronda.NUMERO = Ronda.NUMERO + 1
        self.encuentros = encuentros
        self.promovidos = promovidos or []
        self.tct = tct
        self.nombre = nombre or (self.tct and "Ronda Todos vs Todos" or "Ronda %s" % self.numero);

    #Generar nueva ronda
    @staticmethod
    def generar(robots, tct=False, esc=True, allow_none=False, shuffle=True):
        tct = len(robots) > 2 and tct
        print(tct)
        tuplas = [list(combine) for combine in combinations(robots, 2)]
        ronda_tuplas = []
        if shuffle:
            random.shuffle(tuplas)
        if esc:
            distinta_escuela = [e for e in tuplas if e[0].escuela != e[1].escuela]
            misma_escuela = [e for e in tuplas if e[0].escuela == e[1].escuela]
            tuplas = distinta_escuela + misma_escuela
        for tupla in tuplas:
            if tct or all([not (tupla[0] in encuentro or tupla[1] in encuentro) for encuentro in ronda_tuplas]):
                ronda_tuplas.append(tupla)
            if not tct and len(ronda_tuplas) == len(robots) // 2:
                break
        # Ahora creamos la ronda
        promovidos = set(robots).difference(set(reduce(lambda a, t: a + t, ronda_tuplas, [])))
        if promovidos and allow_none:
            ronda_tuplas = ronda_tuplas + [(p, None) for p in promovidos]
            promovidos = []
        encuentros = [Encuentro(*t) for t in ronda_tuplas]
        return Ronda(encuentros, list(promovidos), tct)

    # Robots
    def get_robots(self):
        return list(reduce(lambda a, e: a.union([e.robot_1, e.robot_2]), self.encuentros, set(self.promovidos)))

    def ganadores(self):
        if self.tct:
            # En una ronda todos contra todos los robots solo son ranqueados,
            # hay que ordenarlos por puntos y obtener una lista de merito
            return self.get_robots()
        else:
            return [e.ganador() for e in self.encuentros] + self.promovidos

    def ganador(self):
        ganadores = self.ganadores()
        if self.finalizado() and len(ganadores) == 1:
            return ganadores.pop()

    def perdedores(self):
        if self.tct:
            # En una ronda todos contra todos los robots solo son ranqueados,
            # hay que ordenarlos por puntos y obtener una lista de merito
            return self.get_robots()
        else:
            return [e.perdedor() for e in self.encuentros]

    def perdedor(self):
        perdedores = self.perdedores()
        if self.finalizado() and len(perdedores) == 1:
            return perdedores.pop()

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

    # Serialize
    def to_dict(self):
        return {
            "encuentros": [ encuentro.to_dict() for encuentro in self.encuentros ],
            "promovidos": self.promovidos,
            "tct": self.tct,
            "nombre": self.nombre
        }

    # Estados
    def iniciado(self):
        return any([e.iniciado() for e in self.get_encuentros()])

    def finalizado(self):
        return all([e.finalizado() for e in self.get_encuentros()])
    
    def compitiendo(self):
        return self.iniciado() and not self.finalizado()

    def jugadas(self):
        return sum([e.jugadas() for e in self.get_encuentros()])

    # Score de la ronda
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
