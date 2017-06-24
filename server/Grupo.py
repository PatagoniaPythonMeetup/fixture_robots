
class Grupo(object):
    def __init__(self):
        self.rondas = []
    
    @staticmethod
    def _generar_grupos(robots, esc=True):
        grupos = []
        escuelas = {re.escuela: [ro for ro in robots if ro.escuela == re.escuela] for re in robots}
        print(escuelas)
        return grupos