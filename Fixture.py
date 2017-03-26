import random
from Encuentro import Encuentro
from functools import reduce

def generador_samu(robots):
    if len(robots) == 2:
        return [Encuentro(robots[0], robots[1])]
    
    _escuela = robots[0].escuela
    _neutros = [r for r in robots if r.escuela==_escuela]
    random.shuffle(_neutros)
    
    _contrincantes = [r for r in robots if r.escuela!=_escuela]
    random.shuffle(_contrincantes)

    _rob_1 = _neutros[0]
    _encuentros = []
    if len(_contrincantes) !=0:
        _rob_2 = _contrincantes[0]
    else:
        _rob_2 = _neutros[1]
    
    robots.remove(_rob_1)
    robots.remove(_rob_2)
    _encuentros.append(Encuentro(_rob_1, _rob_2))
    
    _encuentros.extend(generador_samu(robots))
    
    return _encuentros

def generador_brutus(robots):
    # Producto cartesiano de todos los robots con todos los robots
    encuentros = [Encuentro(r1, r2) for r1 in robots for r2 in robots]
    # Lo barajamos
    random.shuffle(encuentros)
    # Filtramos los que son validos
    encuentros = [encuentro for encuentro in encuentros if encuentro.es_valido()]
    # Filtramos los iguales
    encuentros = reduce(lambda acumulador, encuentro: encuentro in acumulador and acumulador or acumulador + [encuentro], encuentros, [])
    # Quitar los que compite la misma escuela, solo si hay un numero suficiente de encuentros
    encuentros_distintos = [encuentro for encuentro in encuentros if not encuentro.misma_escuela()]
    if len(encuentros_distintos) > len(robots) // 2:
        encuentros = encuentros_distintos
    # Filtramos los encuentros por robot y generamos la ronda
    ronda = []
    _robots = robots[:]
    while _robots:
        encuentro = encuentros.pop()
        if encuentro.robot_1 in _robots and encuentro.robot_2 in _robots:
            _robots.remove(encuentro.robot_1)
            _robots.remove(encuentro.robot_2)
            ronda.append(encuentro)
        elif not encuentros:
            ronda.append(encuentro)
            break
    return ronda

GENERADORES = {
    "samu": generador_samu,
    "brutus": generador_brutus
}

class Fixture(object):
    
    def __init__(self, robots):
        self.robots = robots
        self.rondas = []
        self._generador = GENERADORES["brutus"]

    def ronda(self):
        assert not self.rondas or all([e.finalizado() for e in self.rondas[-1]]), "No se finalizaron los encuentros previos"
        robots = not self.rondas and self.robots or [e for e in self.rondas[-1] if e.ganador() ]
        self.rondas.append(self._generador(robots))
        return len(self.rondas) - 1

    def limpiar(self):
        self.rondas = []

    def encuentros(self, key):
        return self.rondas[key]
    