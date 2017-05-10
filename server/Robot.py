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
        return random.choice(["escudo1.png", "escudo2.png", "escudo3.png"])