from functools import reduce
from .Grupo import Grupo

class Fase(object):
    NUMERO = 1

    def __init__(self, robots, grupos):
        self.numero = Fase.NUMERO
        Fase.NUMERO = Fase.NUMERO + 1
        self.robots = robots
        self.grupos = grupos

    def get_nombre(self):
        return self.__class__.__name__
    
    def get_tipo(self):
        return self.__class__.__name__.lower()
    
    def get_grupos(self):
        return self.grupos[:]

    def get_encuentros(self):
        return reduce(lambda a, ronda: a + ronda.get_encuentros(), self.get_rondas(), [])

    def get_rondas(self):
        return reduce(lambda a, grupo: a + grupo.get_rondas(), self.get_grupos(), [])

    def get_rondas_actuales(self):
        rondas = []
        for grupo in self.get_grupos():
            rondas_del_grupo = grupo.get_rondas()
            if rondas_del_grupo:
                rondas.append(rondas_del_grupo[-1])
        return rondas

    def generar_ronda(self, ngrupo, tct, esc, allow_none, shuffle):
        grupos = [grupo for grupo in self.get_grupos() if grupo.numero == ngrupo]
        if grupos:
            return grupos[0].generar_ronda(tct, esc, allow_none, shuffle)

    def get_robots(self):
        return reduce(lambda a, grupo: a + grupo.get_robots(), self.get_grupos(), [])

    # Estados
    def iniciado(self):
        grupos = self.get_grupos()
        return any([grupo.iniciado() for grupo in grupos])

    def compitiendo(self):
        return self.iniciado() and not self.finalizado()

    def finalizado(self):
        grupos = self.get_grupos()
        return all([grupo.finalizado() for grupo in grupos])

    def ganadores(self):
        robots = reduce(lambda a, grupo: a + grupo.ganadores(), self.get_grupos(), [])
        scores = [(r,) + self.score(r) for r in robots]
        scores = sorted(scores, key=lambda s: s[7] + s[8], reverse=True)
        return [score[0] for score in scores]

    def ganador(self):
        return None

    def perdedores(self):
        robots = reduce(lambda a, grupo: a + grupo.perdedores(), self.get_grupos(), [])
        scores = [(r,) + self.score(r) for r in robots]
        scores = sorted(scores, key=lambda s: s[7] + s[8])
        return [score[0] for score in scores]

    def perdedor(self):
        return None

    def posiciones(self):
        return []

    # Serialize
    def to_dict(self):
        return {
            "nombre": self.get_nombre(),
            "grupos": [grupo.to_dict() for grupo in self.get_grupos()]
        }

    def completar(self):
        return None

    # Trabajando sobre la fase
    def participa(self, robot):
        return any([g.participa(robot) for g in self.get_grupos()])

    def score(self, robot):
        """Retorna el *score* de un robot dentro de la fase
        score es una n-upla de la forma (jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        """
        scores = [grupo.score(robot) for grupo in self.get_grupos()]
        return reduce(lambda acumulador, score: tuple([ a + b for a, b in zip(acumulador, score)]), scores, (0, 0, 0, 0, 0, 0, 0, 0))

class Clasificacion(Fase):
    """Fase en la que los robots son separados en N grupos de donde se tomaran solo a los mas sobresalientes"""
    pass

class Eliminacion(Fase):
    """Fase con un solo grupo donde todos compiten contra todos"""

    def ganador(self):
        return self.grupos[0].ganador()

    def posiciones(self):
        return [
            self.grupos[0].ganador()
            self.grupos[0].perdedor()
        ]

class Final(Fase):
    """Fase donde los robots son separados en dos grupos y se enfrentan hasta quedar dos en la final
    luego se arma la final, tercer y cuarto puesto"""
    NOMBRES = {
        16: "Octavos",
        8: "Cuartos",
        4: "Semifinal",
        2: "Final"
    }

    def __init__(self, robots, grupos):
        grupos = grupos + [Grupo(robots=[], nombre="Tercer y Cuarto"), Grupo(robots=[], nombre=self.NOMBRES[2])]
        super().__init__(robots, grupos)

    def completar(self):
        self.grupos[2].robots = [self.grupos[0].perdedor(), self.grupos[1].perdedor()]
        self.grupos[3].robots = [self.grupos[0].ganador(), self.grupos[1].ganador()]

    def posiciones(self):
        return [
            self.grupos[3].ganador(),   #Primer puesto
            self.grupos[3].perdedor(),  #Segundo puesto
            self.grupos[2].ganador(),   #Tercer puesto
            self.grupos[2].perdedor()   #Cuarto puesto
        ]

    def ganador(self):
        return self.grupos[3].ganador()

class AdHoc(Fase):
    """Fase con dos o mas robots para scorear"""
    pass
