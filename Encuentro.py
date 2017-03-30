
class Encuentro(set):
    def __init__(self, robot_1, robot_2):
        self.robot_1 = robot_1
        self.robot_2 = robot_2
        self.matchs = []


    def raund(self, _robot):
        self.matchs.append(_robot)


    def es_valido(self):
        """Para que el encuentro sea valido los robots deben ser distintos"""
        return self.robot_1 != self.robot_2

    def misma_escuela(self):
        return self.robot_1.escuela == self.robot_2.escuela

    def __eq__(self, other):
        """Un encuentro es igual a otro si tiene los mismos robots"""
        return (self.robot_1 == other.robot_1 and self.robot_2 == other.robot_2) or \
            (self.robot_1 == other.robot_2 and self.robot_2 == other.robot_1)


    def ganador(self):
        r1 = [ r for r in self.matchs if r == self.robot_1 ]
        r2 = [ r for r in self.matchs if r == self.robot_2 ] 
        if len(r1) > len(r2):
            return self.robot_1
        elif len(r1) < len(r2):
            return self.robot_2


    def __str__(self):
        return "<%s vs %s>" % (self.robot_1, self.robot_2)

def main():
    e = Encuentro("1", "2")
    e.raund("1")
    e.raund("2")
    e.raund("2")
    e.raund("1")
    e.raund("1")
    print(e.ganador())

if __name__ == '__main__':
    main()

            