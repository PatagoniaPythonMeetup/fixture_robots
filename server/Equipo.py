import hashlib

from recordclass import recordclass

from .Robot import Robot
from .Participante import Participante

class Equipo(recordclass("Equipo", "robot categoria profesor encargado alumnos escuela escudo peso medidas")):
    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        n_values = 9 - len(args)
        for i in range(n_values):
            args = args + ("undefined",)
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(self, *args):
        for attr in self.__slots__:
            setattr(self, attr, self.def_value)
    
    def name(self):
        return self.robot.nombre

    def __str__(self):
        return self.robot.nombre

    @property
    def key(self):
        _key = self.robot.nombre + self.escuela + self.encargado.nombre
        return hashlib.md5(_key.encode("utf-8")).hexdigest()
    
    def __eq__(self, other):
        return isinstance(other, Equipo) and self.key == other.key 