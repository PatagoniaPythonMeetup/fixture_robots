import random
from Encuentro import Encuentro
from Ronda import Ronda
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

def generador_combinaciones(robots):
    def potencia(c):
        if len(c) == 0:
            return [[]]
        r = potencia(c[:-1])
        return r + [s + [c[-1]] for s in r]
    def combinaciones(rs, n):
        return [s for s in potencia(rs) if len(s) == n]
    encuentros = [Encuentro(*e) for e in combinaciones(robots, 2)]
    ronda = []
    random.shuffle(encuentros)
    distinta_escuela = [ e for e in encuentros if not e.misma_escuela() ]
    misma_escuela = [ e for e in encuentros if e.misma_escuela() ]
    for _encuentros in [distinta_escuela, misma_escuela]:
        while _encuentros:
            encuentro = _encuentros.pop()
            if all([not (e.participa(encuentro.robot_1) or e.participa(encuentro.robot_2)) for e in ronda]):
                ronda.append(encuentro)
            if len(ronda) == len(robots) // 2:
                break
    return ronda

GENERADORES = {
    "samu": generador_samu,
    "brutus": generador_brutus,
    "combinaciones": generador_combinaciones
}

class Fixture(object):

    def __init__(self, robots):
        self.robots = robots
        self.rondas = []
        self._generador = GENERADORES["combinaciones"]

    def ronda(self):
        assert not self.rondas or self.rondas[-1].finalizada(), "No se finalizo la ultima ronda"
        robots = self.robots if not self.rondas else self.rondas[-1].ganadores()
        encuentros = self._generador(robots)
        promovidos = set(robots).difference(set(reduce(lambda a, e: a + [e.robot_1] + [e.robot_2], encuentros, [])))
        ronda = Ronda(len(self.rondas) + 1, encuentros, list(promovidos))
        self.rondas.append(ronda)
        return ronda

    def limpiar(self):
        self.rondas = []
    
    def get_ronda(self, numero):
        return self.rondas[numero - 1]

    def finalizado(self):
        """Un fixture esta finalizado cuando todas las rondas estan finalizadas y la ultima ronda tiene a un solo ganador"""
        return self.rondas and all([r.finalizada() for r in self.rondas]) and len(self.rondas[-1].ganadores()) == 1

    def ganador(self):
        return self.rondas[-1].ganadores().pop()