import graphene
from graphene import resolve_only_args

class Estado(graphene.ObjectType):
    iniciado = graphene.Boolean()
    compitiendo = graphene.Boolean()
    finalizado = graphene.Boolean()
    vuelta = graphene.Int()
    jugadas = graphene.Int()
    encuentros = graphene.List(graphene.Int)
    ronda = graphene.Int()

    def resolve_iniciado(self, args, context, info):
        return self.iniciado()

    def resolve_compitiendo(self, args, context, info):
        return self.compitiendo()
    
    def resolve_finalizado(self, args, context, info):
        return self.finalizado()

    def resolve_vuelta(self, args, context, info):
        return self.vuelta()

    def resolve_jugadas(self, args, context, info):
        return self.jugadas()
    
    def resolve_encuentros(self, args, context, info):
        encuentros = self.get_encuentros_actuales()
        return [e.numero for e in encuentros]

    def resolve_ronda(self, args, context, info):
        ronda = self.get_ronda_actual()
        return ronda.numero if ronda is not None else 0
    
class Robot(graphene.ObjectType):
    key = graphene.String()
    nombre = graphene.String()
    escuela = graphene.String()
    encargado = graphene.String()
    escudo = graphene.String()
    score = graphene.List(graphene.Int)

    def resolve_score(self, args, context, info):
        fixture = context["fixture"]
        robot = fixture.get_robot_por_key(self.key)
        return fixture.score(robot)

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
    nombre = graphene.String()
    numero = graphene.Int()
    robots = graphene.List(Robot)
    grupos = graphene.List(Grupo)
    score = graphene.List(graphene.Int, key=graphene.Argument(graphene.NonNull(graphene.String)))
    scores = graphene.List(graphene.List(graphene.Int))
    estado = graphene.Field(Estado)

    def resolve_robots(self, args, context, info):
        return self.get_robots()

    def resolve_nombre(self, args, context, info):
        return self.get_nombre()

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
    robot = graphene.Field(Robot, key=graphene.Argument(graphene.NonNull(graphene.String)))
    robots = graphene.List(Robot)
    encuentro = graphene.Field(Encuentro, numero=graphene.Argument(graphene.Int))
    encuentros = graphene.List(Encuentro)
    ronda = graphene.Field(Ronda, numero=graphene.Argument(graphene.Int))
    rondas = graphene.List(Ronda)
    fase = graphene.Field(Fase, numero=graphene.Argument(graphene.Int))
    fases = graphene.List(Fase)
    ganador = graphene.Field(Robot)
    score = graphene.List(graphene.Int, key=graphene.Argument(graphene.NonNull(graphene.String)))
    scores = graphene.List(graphene.List(graphene.Int))
    estado = graphene.Field(Estado)

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
        grupos = graphene.Int()
        
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        grupos = args.get('grupos')
        try:
            fase = fixture.clasificacion(grupos)
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
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        try:
            fase = fixture.final()
            return GenerarFinal(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            return GenerarFinal(ok = False, mensaje = str(ex), estado = fixture)

class GenerarRondas(graphene.Mutation):
    class Input:
        tct = graphene.Boolean()
        allow_none = graphene.Boolean()
        shuffle = graphene.Boolean()
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    rondas = graphene.List(Ronda)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        tct = args.get('tct')
        allow_none = args.get('allow_none')
        shuffle = args.get('shuffle')
        try:
            rondas = fixture.generar_rondas(tct, allow_none, shuffle)
            return GenerarRondas(ok = True, mensaje = "Ronda creada", rondas = rondas, estado = fixture)
        except Exception as ex:
            return GenerarRondas(ok = False, mensaje = str(ex), estado = fixture)

class AgregarGanador(graphene.Mutation):
    class Input:
        key = graphene.String()
        encuentro = graphene.Int()
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    encuentro = graphene.Field(lambda: Encuentro)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        key = args.get('key')
        encuentro = args.get('encuentro')
        try:
            robot = fixture.get_robot_por_key(key)
            encuentro = fixture.agregar_ganador(robot, nencuentro=encuentro)
            return AgregarGanador(ok = True, mensaje = "Robot declarado ganador", encuentro = encuentro, estado = fixture)
        except Exception as ex:
            return AgregarGanador(ok = False, mensaje = str(ex), estado = fixture)

class QuitarGanador(graphene.Mutation):
    class Input:
        key = graphene.String()
        encuentro = graphene.Int()
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    encuentro = graphene.Field(lambda: Encuentro)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, args, context, info):
        fixture = context["fixture"]
        key = args.get('key')
        encuentro = args.get('encuentro')
        try:
            robot = fixture.get_robot_por_key(key)
            encuentro = fixture.quitar_ganador(robot, nencuentro=encuentro)
            return AgregarGanador(ok = True, mensaje = "Robot no declarado ganador", encuentro = encuentro, estado = fixture)
        except Exception as ex:
            return AgregarGanador(ok = False, mensaje = str(ex), estado = fixture)

class Mutations(graphene.ObjectType):
    generar_clasificacion = GenerarClasificacion.Field()
    generar_eliminacion = GenerarEliminacion.Field()
    generar_final = GenerarFinal.Field()
    generar_rondas = GenerarRondas.Field()
    agregar_ganador = AgregarGanador.Field()
    quitar_ganador = QuitarGanador.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
