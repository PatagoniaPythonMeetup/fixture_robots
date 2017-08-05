from collections import namedtuple
import hashlib
import random
import itertools


class Participante(namedtuple("Participante", "nombre dni email rol")):
    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        if len(args) == 3: 
            args = args + ("alumno")
        elif args[3] is None:
            args = args[:3] + ("alumno")
        return super().__new__(cls, *args, **kwargs)

        def __str__(self):
            return "{}\n{}".format(self.nombre, self.dni)
    @property
    def key(self):
        _key = self.nombre + self.dni
        return hashlib.md5(_key.encode("utf-8")).hexdigest()

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return isinstance(other, Participante) and self.key == other.key
