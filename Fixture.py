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
    
    _encuentros.extend(self._generar_encuentros(robots))
    
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
    # Quitar los que conpite la misma escuela
    encuentros = filter(lambda encuentro: not encuentro.misma_escuela(), encuentros)

    return encuentros

GENERADORES = {
    "samu": generador_samu,
    "brutus": generador_brutus
}

class Fixture(object):
    
    def __init__(self, robots):
        self.robots = robots
        self.rondas = []
        self._generador = GENERADORES["brutus"]


    def vencedor(self, robot):
        pass


    def ronda(self):
        robots = not self.rondas and self.robots or [e for e in self.rondas[-1] if e.ganador() ]
        self.rondas.append(self._generador(robots))


    def encuentros(self, ronda):
        return self.rondas[ronda]
    

    def cambiar_ronda(self, _robots_ganadores):
        """ Avanza de ronda, generando los encuentros entre los robots ganadores
            Pre:
            Post: """
        print("Robots en juego:\n".format(_robots_ganadores))
        _encuentros_ronda = self.generar_encuentros(self.robots.copy())
        self.encuentros.append(_encuentros_ronda)
        return
    