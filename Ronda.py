
class Ronda(object):
    def __init__(self, numero, encuentros):
        self.numero = numero
        self.encuentros = encuentros

    def finalizada(self):
        return all([e.finalizado() for e in self.encuentros])