from collections import namedtuple

class Robot(namedtuple("Robot", "nombre escuela encargado")):
    __slots__ = ()
    @property
    def key(self):
        return abs(hash(self)) % 10000