from collections import namedtuple
import hashlib
import random

class Robot(namedtuple("Robot", "nombre escuela encargado")):
    __slots__ = ()
    
    @property
    def key(self):
        _key = self.nombre + self.escuela + self.encargado
        return hashlib.md5(_key.encode("utf-8")).hexdigest()
    
    @property
    def escudo(self):
        return random.choice(["e{0:02d}.png".format(numero) for numero in range(1, 23)])