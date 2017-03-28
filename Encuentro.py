
class Encuentro(object):
    def __init__(self, robot_1, robot_2):
        self.robot_1 = robot_1
        self.robot_2 = robot_2
        self.ganadas = []

    def puntaje(self, robot):
        assert robot is self.robot_1 or robot is self.robot_2, "El robot ganador no es parte del encuentro"
        victorias = len([r for r in self.ganadas if r == robot])
        derrotas = len([r for r in self.ganadas if r != robot])
        return victorias, derrotas

    def gano(self, robot):
        assert robot is self.robot_1 or robot is self.robot_2, "El robot ganador no es parte del encuentro"
        self.ganadas.append(robot)

    def es_valido(self):
        """Para que el encuentro sea valido los robots deben ser distintos"""
        return self.robot_1 != self.robot_2

    def misma_escuela(self):
        return self.robot_1.escuela == self.robot_2.escuela

    def __eq__(self, other):
        """Un encuentro es igual a otro si tiene los mismos robots"""
        return hash(self) == hash(other)
        
    def finalizado(self):
        return self.ganador() != None

    def ganador(self):
        r1 = [ r for r in self.ganadas if r == self.robot_1 ]
        r2 = [ r for r in self.ganadas if r == self.robot_2 ] 
        if len(r1) > len(r2):
            return self.robot_1
        elif len(r1) < len(r2):
            return self.robot_2

    def participa(self, valor):
        return valor == self.robot_1 or valor in self.robot_1 or valor == self.robot_2 or valor in self.robot_2

    def __str__(self):
        return "<%s vs %s>" % (self.robot_1, self.robot_2)
    
    def __hash__(self):
        return hash(self.robot_1) + hash(self.robot_2) 

def main():
    e = Encuentro("1", "2")
    e.gano("1")
    e.gano("2")
    e.gano("2")
    e.gano("1")
    e.gano("2")
    print(e.ganador(), e.puntaje("1"), e.puntaje("2"))

if __name__ == '__main__':
    main()

            