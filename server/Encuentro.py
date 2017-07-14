

class Encuentro(object):
    """Un encuentro enfrenta a dos competidores"""
    JUGADAS = 3
    NUMERO = 1
    def __init__(self, robot_1, robot_2=None, ganadas=None):
        self.robot_1 = robot_1
        self.robot_2 = robot_2
        self.numero = Encuentro.NUMERO
        Encuentro.NUMERO = Encuentro.NUMERO + 1
        self.ganadas = ganadas or []

    def score(self, robot):
        """El score de un robot en un encuentro se obtiene en base a las victorias y derrotas"""
        assert robot == self.robot_1 or robot == self.robot_2, "El robot ganador no es parte del encuentro"
        if not self.ganadas:
            return 0, 0
        victorias = len([r for r in self.ganadas if r == robot])
        derrotas = len([r for r in self.ganadas if r != robot])
        return victorias, derrotas

    def agregar_ganador(self, robot):
        assert robot == self.robot_1 or robot == self.robot_2, "El robot no es parte del encuentro"
        self.ganadas.append(robot)

    def quitar_ganador(self, robot):
        assert robot in self.ganadas, "El robot no gano en este encuentro"
        self.ganadas.remove(robot)

    def es_valido(self):
        """Para que el encuentro sea valido los robots deben ser distintos"""
        return self.robot_2 is not None and self.robot_1 != self.robot_2

    def misma_escuela(self):
        return self.robot_2 is not None and self.robot_1.escuela == self.robot_2.escuela

    def __eq__(self, other):
        """Un encuentro es igual a otro si tiene los mismos robots"""
        return hash(self) == hash(other)

    # Estados
    def iniciado(self):
        return self.robot_2 is not None and not self.finalizado()

    def finalizado(self):
        numero_jugadas = self.jugadas()
        tiene_ganador = bool(self.ganador())
        score = self.score(self.robot_1)
        return (numero_jugadas >= self.JUGADAS and tiene_ganador) or (tiene_ganador and abs(score[0] - score[1]) > 1)

    def compitiendo(self):
        return not self.finalizado()

    def vuelta(self):
        return len(self.ganadas)

    def jugadas(self):
        return len(self.ganadas)

    def ganador(self):
        r1 = [ r for r in self.ganadas if r == self.robot_1 ]
        r2 = [ r for r in self.ganadas if r == self.robot_2 ] 
        if len(r1) > len(r2):
            return self.robot_1
        elif len(r1) < len(r2):
            return self.robot_2

    def perdedor(self):
        ganador = self.ganador()
        if ganador:
            return self.robot_1 if self.robot_2 == ganador else self.robot_2

    def participa(self, valor):
        return valor == self.robot_1 or valor in self.robot_1 or valor == self.robot_2 or valor in self.robot_2

    def to_dict(self):
        return {
            "robot_1": self.robot_1,
            "robot_2": self.robot_2,
            "ganadas": self.ganadas
        }

    def __str__(self):
        return "<%s[%s] vs %s[%s]>" % (self.robot_1.nombre, self.score(self.robot_1), self.robot_2.nombre, self.score(self.robot_2))

    def __hash__(self):
        return hash(self.robot_1) + hash(self.robot_2)
            