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

    def participa(self, robot):
        return robot in self.promovidos or any([e.participa(robot) for e in self.encuentros])

    def finalizada(self):
        return all([e.finalizado() for e in self.encuentros])

    def ganadores(self):
        return [e.ganador() for e in self.encuentros] + self.promovidos
    
    def get_encuentro(self, numero):
        encuentros = [encuentro for encuentro in self.encuentros if encuentro.numero == numero]
        if encuentros:
            return encuentros.pop()
    
    def gano(self, robot):
        encuentros = [encuentro for encuentro in self.encuentros if encuentro.participa(robot)]
        assert len(encuentros) == 1, "El robot no participa de la ronda"
        encuentros[0].gano(robot)

    def vuelta(self):
        return max([e.jugadas() for e in self.encuentros])
    
    def jugadas(self):
        return sum([e.jugadas() for e in self.encuentros])

    def to_dict(self):
        return {
            "numero": self.numero,
            "encuentros": [ encuentro.to_dict() for encuentro in self.encuentros ],
            "promovidos": self.promovidos
        }