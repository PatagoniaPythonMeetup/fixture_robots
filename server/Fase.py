
class Fase(object):
    def __init__(self, robots):
        self.robots = robots

class FaseGrupo(Fase):
    def __init__(self, robots):
        super().__init__(robots)
        self.grupos = []

class FaseEliminacion(Fase):
    def __init__(self, robots):
        super().__init__(robots)
        self.rondas = []

class FaseFinal(Fase):
    def __init__(self, robots):
        super().__init__(robots)
