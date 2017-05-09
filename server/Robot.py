from collections import namedtuple

class Robot(namedtuple("Robot", "nombre escuela encargado")):
    __slots__ = ()
    @property
    def key(self):
        return str(abs(hash(self.nombre)) % 10000)