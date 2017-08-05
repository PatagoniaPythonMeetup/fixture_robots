import Robot
import Participante

class Equipo(namedtuple("Equipo", "robot categoria profesor encargado alumnos escuela escudo")):
	__slots__ = ()

	# @validate_equipo()
    def __new__(cls, *args, **kwargs):
	# def __init__(self, un_robot, una_categoria, un_profesor, un_encargado, alumnos, nombre_escuela, ruta_escudo): #arg):
		return super().__new__(cls, *args, **kwargs)

	def name(self):
		return self.robot.name

	def __str__(self):
		return self.robot.name


def validate_equipo():
    def decorate(func):
        def funcDecorated(*args, **kwargs):
            types = [Robot, str, Participante, Participante, list, str, str]
            newArgs = list(args)
            assert ( ( len(newArgs) == len(types) ) or ( len(newArgs) == (len(types)-1) ) ), "Cantidad incompatible de argumentos({}, [{}])".format(len(newArgs), newArgs)
            for i, (a, t) in enumerate(zip(newArgs, types)):
                assert type(a) == t, "Arg Nº{} must be type: {}".format(i, t)
            profesor = newArgs[2]
            for alumno in newArgs[4]:
                assert type(alumno) == Participante, "Arg Nº4 must contain only instances of Alumno"
                assert alumno != profesor, "El rol de 'Profesor' no puede ser cumplido por uno de los alumnos"
            # wrong arguments!
            else:
                return func(*newArgs, **kwargs)

        return funcDecorated
    return decorate