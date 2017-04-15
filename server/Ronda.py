from functools import reduce

from .Robot import Robot

class Ronda(object):
    def __init__(self, numero, encuentros, promovidos=None):
        self.numero = numero
        self.encuentros = encuentros
        self.promovidos = promovidos or []

    @property
    def robots(self):
        return reduce(lambda a, e: a + [e.robot_1] + [e.robot_2], self.encuentros, self.promovidos)

    def finalizada(self):
        return all([e.finalizado() for e in self.encuentros])

    def ganadores(self):
        return [e.ganador() for e in self.encuentros] + self.promovidos
    
    def get_encuentro(self, valor):
        encuentros = [encuentro for encuentro in self.encuentros if (isinstance(valor, int) and encuentro.numero == valor) or encuentro.participa(valor)]
        if encuentros:
            return encuentros.pop()
    
    def gano(self, nronda, nencuentro, nrobot):
        robot = get_robot_por_nombre(nrobot)
        ronda = get_ronda(nronda)
        if ronda is not None:
            ronda.gano(nencuentro, robot)

    def gano(self, nencuentro, robot):
        assert robot in self.robots, "El robot ganador no es parte de la ronda"
        encuentro = self.get_encuentro(nencuentro)
        if encuentro is not None:
            encuentro.gano(robot)
    
    def vuelta(self):
        return max([e.jugadas() for e in self.encuentros])
    
    def jugadas(self):
        return sum([e.jugadas() for e in self.encuentros])

    def score(self, robot):
        """El score de un robot en una ronda es el score del encuentro en donde participo ese robot"""
        encuentro = self.get_encuentro(robot)
        return encuentro.score(robot) if encuentro is not None else (0, 0, 0)

    def to_dict(self):
        return {
            "numero": self.numero,
            "encuentros": [ encuentro.to_dict() for encuentro in self.encuentros ],
            "promovidos": self.promovidos
        }