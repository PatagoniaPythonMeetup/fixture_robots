from functools import reduce

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