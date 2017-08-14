import graphene
import traceback
from graphene import resolve_only_args

class Estado(graphene.ObjectType):
    iniciado = graphene.Boolean()
    compitiendo = graphene.Boolean()
    finalizado = graphene.Boolean()
    jugadas = graphene.Int()
    encuentros = graphene.List(graphene.Int)
    ronda = graphene.Int()

    def resolve_iniciado(self, args, context, info):
        return self.iniciado()

    def resolve_compitiendo(self, args, context, info):
        return self.compitiendo()
    
    def resolve_finalizado(self, args, context, info):
        return self.finalizado()

    def resolve_jugadas(self, args, context, info):
        return self.jugadas()
    
    def resolve_encuentros(self, args, context, info):
        encuentros = self.get_encuentros_actuales()
        return [e.numero for e in encuentros]

    def resolve_ronda(self, args, context, info):
        ronda = self.get_ronda_actual()
        return ronda.numero if ronda is not None else 0

class Participante(graphene.ObjectType):
    nombre = graphene.String()
    dni = graphene.String()
    email = graphene.String()
    rol = graphene.String()

class Robot(graphene.ObjectType):
    key = graphene.String()
    nombre = graphene.String()
    escuela = graphene.String()
    encargado = graphene.Field(Participante)
    escudo = graphene.String()

    def resolve_estado(self, args, context, info):
        return self.encargado

class Equipo(graphene.ObjectType):
    robot = graphene.Field(Robot)
    categoria = graphene.String()
    profesor = graphene.Field(Participante)
    encargado = graphene.Field(Participante)
    alumnos = graphene.List(Participante)
    escuela = graphene.String()
    escudo = graphene.String()
    peso = graphene.String()
    medidas = graphene.String()

    def resolve_estado(self, args, context, info):
        return self.encargado

class Encuentro(graphene.ObjectType):
    numero = graphene.Int()
    robots = graphene.List(Robot)
    estado = graphene.Field(Estado)
    puntos = graphene.List(graphene.Int)

    def resolve_robots(self, args, context, info):
        return [self.robot_1, self.robot_2]

    def resolve_puntos(self, args, context, info):
        return self.score(self.robot_1)

    def resolve_estado(self, args, context, info):
        return self

class Ronda(graphene.ObjectType):
    robots = graphene.List(Robot)
    numero = graphene.Int()
    encuentros = graphene.List(Encuentro)
    promovidos = graphene.List(Robot)
    tct = graphene.Boolean()
    score = graphene.List(graphene.Int, key=graphene.Argument(graphene.NonNull(graphene.String)))
    scores = graphene.List(graphene.List(graphene.Int))
    estado = graphene.Field(Estado)

    def resolve_robots(self, args, context, info):
        return self.get_robots()

    def resolve_score(self, args, context, info):
        key = args['key']
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_scores(self, args, context, info):
        return [self.score(robot) for robot in self.get_robots()]

    def resolve_estado(self, args, context, info):
        return self

class Grupo(graphene.ObjectType):
    numero = graphene.Int()
    robots = graphene.List(Robot)
    rondas = graphene.List(Ronda)
    score = graphene.List(graphene.Int, key=graphene.Argument(graphene.NonNull(graphene.String)))
    scores = graphene.List(graphene.List(graphene.Int))
    estado = graphene.Field(Estado)

    def resolve_robots(self, args, context, info):
        return self.get_robots()

    def resolve_rondas(self, args, context, info):
        return self.get_rondas()

    def resolve_score(self, args, context, info):
        key = args['key']
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_scores(self, args, context, info):
        return [self.score(robot) for robot in self.get_robots()]

    def resolve_estado(self, args, context, info):
        return self

class Fase(graphene.ObjectType):
    tipo = graphene.String()
    nombre = graphene.String()
    numero = graphene.Int()
    robots = graphene.List(Robot)
    grupos = graphene.List(Grupo)
    score = graphene.List(graphene.Int, key=graphene.Argument(graphene.NonNull(graphene.String)))
    scores = graphene.List(graphene.List(graphene.Int))
    estado = graphene.Field(Estado)

    def resolve_tipo(self, args, context, info):
        return self.get_tipo()

    def resolve_nombre(self, args, context, info):
        return self.get_nombre()

    def resolve_robots(self, args, context, info):
        return self.get_robots()

    def resolve_class(self, args, context, info):
        key = args['key']
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_score(self, args, context, info):
        key = args['key']
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_scores(self, args, context, info):
        return [self.score(robot) for robot in self.get_robots()]

    def resolve_estado(self, args, context, info):
        return self

class Fixture(graphene.ObjectType):
    estado = graphene.Field(Estado)
    robot = graphene.Field(Robot, key=graphene.Argument(graphene.NonNull(graphene.String)))
    robots = graphene.List(Robot)
    fase = graphene.Field(Fase, numero=graphene.Argument(graphene.Int))
    fases = graphene.List(Fase)
    ronda = graphene.Field(Ronda, numero=graphene.Argument(graphene.Int))
    rondas = graphene.List(Ronda)
    encuentro = graphene.Field(Encuentro, numero=graphene.Argument(graphene.Int))
    encuentros = graphene.List(Encuentro)
    score = graphene.List(graphene.Int, key=graphene.Argument(graphene.NonNull(graphene.String)))
    scores = graphene.List(graphene.List(graphene.Int))
    ganador = graphene.Field(Robot)

    def resolve_robot(self, args, context, info):
        key = args['key']
        return self.get_robot_por_key(key)

    def resolve_robots(self, args, context, info):
        return self.get_robots()

    def resolve_encuentro(self, args, context, info):
        numero = args['numero']
        return self.get_encuentro(numero)

    def resolve_encuentros(self, args, context, info):
        return self.get_encuentros()

    def resolve_ronda(self, args, context, info):
        numero = args['numero']
        return self.get_ronda(numero)

    def resolve_rondas(self, args, context, info):
        return self.get_rondas()

    def resolve_fase(self, args, context, info):
        numero = args['numero']
        return self.get_fase(numero)

    def resolve_fases(self, args, context, info):
        return self.get_fases()

    def resolve_ganador(self, args, context, info):
        return self.ganador()
    
    def resolve_score(self, args, context, info):
        key = args['key']
        fixture = context["fixture"]
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_scores(self, args, context, info):
        return [self.score(robot) for robot in self.get_robots()]

    def resolve_estado(self, args, context, info):
        return self

class Query(graphene.ObjectType):
    fixture = graphene.Field(Fixture)

    def resolve_fixture(self, args, context, info):
        return context["fixture"]

# Mutaciones
class GenerarClasificacion(graphene.Mutation):
    class Input:
        grupos = graphene.NonNull(graphene.Int)
        esc = graphene.Boolean()
        
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        grupos = args.get('grupos')
        esc = args.get('esc') or True
        try:
            fase = fixture.clasificacion(grupos, esc)
            return GenerarClasificacion(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            return GenerarClasificacion(ok = False, mensaje = str(ex), estado = fixture)

class GenerarEliminacion(graphene.Mutation):
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        try:
            fase = fixture.eliminacion()
            return GenerarEliminacion(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            return GenerarEliminacion(ok = False, mensaje = str(ex), estado = fixture)

class GenerarFinal(graphene.Mutation):
    class Input:
        jugadores = graphene.NonNull(graphene.Int)
        
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        jugadores = args.get('jugadores')
        try:
            fase = fixture.final(jugadores)
            return GenerarFinal(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            return GenerarFinal(ok = False, mensaje = str(ex), estado = fixture)

class GenerarAdHoc(graphene.Mutation):
    class Input:
        robots = graphene.List(graphene.String)
        
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        robots = args.get('robots')
        try:
            fase = fixture.adhoc(robots)
            return GenerarFinal(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            return GenerarFinal(ok = False, mensaje = str(ex), estado = fixture)

class GenerarRonda(graphene.Mutation):
    class Input:
        grupo = graphene.NonNull(graphene.Int)
        tct = graphene.Boolean()
        esc = graphene.Boolean()
        allow_none = graphene.Boolean()
        shuffle = graphene.Boolean()
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    ronda = graphene.Field(Ronda)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        ngrupo = args.get('grupo')
        tct = args.get('tct') or False
        esc = args.get('esc') or True
        allow_none = args.get('allow_none') or False
        shuffle = args.get('shuffle') or True
        try:
            ronda = fixture.generar_ronda(ngrupo, tct, esc, allow_none, shuffle)
            return GenerarRonda(ok = True, mensaje = "Ronda creada", ronda = ronda, estado = fixture)
        except Exception as ex:
            return GenerarRonda(ok = False, mensaje = str(ex), estado = fixture)

class AgregarGanador(graphene.Mutation):
    class Input:
        key = graphene.NonNull(graphene.String)
        encuentro = graphene.NonNull(graphene.Int)
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    encuentro = graphene.Field(lambda: Encuentro)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        key = args.get('key')
        nencuentro = args.get('encuentro')
        try:
            robot = fixture.get_robot_por_key(key)
            encuentro = fixture.agregar_ganador(robot, nencuentro)
            return AgregarGanador(ok = True, mensaje = "Robot declarado ganador", encuentro = encuentro, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return AgregarGanador(ok = False, mensaje = str(ex), estado = fixture)

class QuitarGanador(graphene.Mutation):
    class Input:
        key = graphene.NonNull(graphene.String)
        encuentro = graphene.NonNull(graphene.Int)
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    encuentro = graphene.Field(lambda: Encuentro)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        key = args.get('key')
        nencuentro = args.get('encuentro')
        try:
            robot = fixture.get_robot_por_key(key)
            encuentro = fixture.quitar_ganador(robot, nencuentro)
            return AgregarGanador(ok = True, mensaje = "Robot no declarado ganador", encuentro = encuentro, estado = fixture)
        except Exception as ex:
            return AgregarGanador(ok = False, mensaje = str(ex), estado = fixture)

class AgregarAdversario(graphene.Mutation):
    class Input:
        encuentro = graphene.NonNull(graphene.Int)
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    encuentro = graphene.Field(lambda: Encuentro)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        nencuentro = args.get('encuentro')
        try:
            encuentro = fixture.agregar_adversario(nencuentro)
            return AgregarGanador(ok = True, mensaje = "Encuentro resuelto con nuevo adversario", encuentro = encuentro, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return AgregarGanador(ok = False, mensaje = str(ex), estado = fixture)

class Mutations(graphene.ObjectType):
    generar_clasificacion = GenerarClasificacion.Field()
    generar_eliminacion = GenerarEliminacion.Field()
    generar_final = GenerarFinal.Field()
    generar_adhoc = GenerarAdHoc.Field()
    generar_ronda = GenerarRonda.Field()
    agregar_ganador = AgregarGanador.Field()
    quitar_ganador = QuitarGanador.Field()
    agregar_adversario = AgregarAdversario.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
