from collections import namedtuple
import hashlib
import random

# FIXME: Solo tenemos por el momento 23 imagenes
IMGS = ["e{0:02d}.png".format(numero) for numero in range(1, 23)]

class Robot(namedtuple("Robot", "nombre escuela encargado escudo")):
    __slots__ = ()
    
    def __new__(cls, *args, **kwargs):
        if len(args) == 3:
            args = args + (IMGS.pop(random.randint(0, len(IMGS) - 1)), )
        return super().__new__(cls, *args, **kwargs)

    @property
    def key(self):
        _key = self.nombre + self.escuela + self.encargado
        return hashlib.md5(_key.encode("utf-8")).hexdigest()
