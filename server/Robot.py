from collections import namedtuple
import hashlib
import random
import itertools

NUMEROS = itertools.count()
IMAGENES = 22

class Robot(namedtuple("Robot", "nombre escuela encargado escudo")):
    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        if len(args) == 3:
            args = args + ("e{0:02d}.png".format((next(NUMEROS) % IMAGENES) + 1), )
        elif args[3] is None:
            args = args[:3] + ("e{0:02d}.png".format((next(NUMEROS) % IMAGENES) + 1), )
        return super().__new__(cls, *args, **kwargs)

    @property
    def key(self):
        _key = self.nombre + self.escuela + self.encargado
        return hashlib.md5(_key.encode("utf-8")).hexdigest()

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return isinstance(other, Robot) and self.key == other.key
