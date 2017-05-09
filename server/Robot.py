from collections import namedtuple

class Robot(namedtuple("Robot", "nombre escuela encargado")):
    __slots__ = ()
    @property
    def key(self):
        k = self.nombre + self.escuela + self.encargado
        print(k)
        return hash(k)