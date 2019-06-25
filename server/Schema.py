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

    def resolve_iniciado(self, info):
        return self.iniciado()

    def resolve_compitiendo(self, info):
        return self.compitiendo()
    
    def resolve_finalizado(self, info):
        return self.finalizado()

    def resolve_jugadas(self, info):
        return self.jugadas()
    
    def resolve_encuentros(self, info):
        encuentros = self.get_encuentros_actuales()
        return [e.numero for e in encuentros]

    def resolve_ronda(self, info):
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

    def resolve_estado(self, info):
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
    puntos = graphene.Int()

    def resolve_estado(self, info):
        return self.encargado

    def resolve_puntos(self, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        score = fixture.score(self.robot)
        return score[7]

class Encuentro(graphene.ObjectType):
    numero = graphene.Int()
    robots = graphene.List(Robot)
    estado = graphene.Field(Estado)
    puntos = graphene.List(graphene.Int)

    def resolve_robots(self, info):
        return [self.robot_1, self.robot_2]

    def resolve_puntos(self, info):
        return self.score(self.robot_1)

    def resolve_estado(self, info):
        return self

class Ronda(graphene.ObjectType):
    robots = graphene.List(Robot)
    nombre = graphene.String()
    numero = graphene.Int()
    encuentros = graphene.List(Encuentro)
    promovidos = graphene.List(Robot)
    tct = graphene.Boolean()
    score = graphene.List(graphene.Int, key=graphene.Argument(graphene.NonNull(graphene.String)))
    scores = graphene.List(graphene.List(graphene.Int))
    estado = graphene.Field(Estado)

    def resolve_robots(self, info):
        return self.get_robots()

    def resolve_score(self, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        key = kwargs['key']
        robot = context["fixture"].get_robot_por_key(key)
        return self.score(robot)

    def resolve_scores(self, info):
        return [self.score(robot) for robot in self.get_robots()]

    def resolve_estado(self, info):
        return self

class Grupo(graphene.ObjectType):
    numero = graphene.Int()
    nombre = graphene.String()
    robots = graphene.List(Robot)
    rondas = graphene.List(Ronda)
    score = graphene.List(graphene.Int, key=graphene.Argument(graphene.NonNull(graphene.String)))
    scores = graphene.List(graphene.List(graphene.Int))
    estado = graphene.Field(Estado)

    def resolve_robots(self, info):
        return self.get_robots()

    def resolve_rondas(self, info):
        return self.get_rondas()

    def resolve_score(self, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        key = kwargs['key']
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_scores(self, info):
        return [self.score(robot) for robot in self.get_robots()]

    def resolve_estado(self, info):
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

    def resolve_tipo(self, info):
        return self.get_tipo()

    def resolve_nombre(self, info):
        return self.get_nombre()

    def resolve_robots(self, info):
        return self.get_robots()

    def resolve_class(self, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        key = kwargs['key']
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_score(self, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        key = kwargs['key']
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_scores(self, info):
        return [self.score(robot) for robot in self.get_robots()]

    def resolve_estado(self, info):
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
    posiciones = graphene.List(Equipo)

    def resolve_robot(self, info, *args, **kwargs):
        key = kwargs['key']
        return self.get_robot_por_key(key)

    def resolve_robots(self, info):
        return self.get_robots()

    def resolve_encuentro(self, info, *args, **kwargs):
        numero = kwargs['numero']
        return self.get_encuentro(numero)

    def resolve_encuentros(self, info):
        return self.get_encuentros()

    def resolve_ronda(self, info, *args, **kwargs):
        numero = kwargs['numero']
        return self.get_ronda(numero)

    def resolve_rondas(self, info):
        return self.get_rondas()

    def resolve_fase(self, info, *args, **kwargs):
        numero = kwargs['numero']
        return self.get_fase(numero)

    def resolve_fases(self, info):
        return self.get_fases()

    def resolve_ganador(self, info):
        return self.ganador()
    
    def resolve_posiciones(self, info):
        return self.posiciones()

    def resolve_score(self, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        key = kwargs['key']
        robot = fixture.get_robot_por_key(key)
        return self.score(robot)

    def resolve_scores(self, info):
        return [self.score(robot) for robot in self.get_robots()]

    def resolve_estado(self, info):
        return self

class Query(graphene.ObjectType):
    fixture = graphene.Field(Fixture)

    def resolve_fixture(self, info, *args, **kwargs):
        print(info)
        return info.context["fixture"]

# Mutaciones
class GenerarClasificacion(graphene.Mutation):
    class Input:
        grupos = graphene.NonNull(graphene.Int)
        esc = graphene.NonNull(graphene.Boolean)
        
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        grupos = kwargs['grupos']
        esc = kwargs['esc']
        try:
            fase = fixture.clasificacion(grupos, esc)
            return GenerarClasificacion(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return GenerarClasificacion(ok = False, mensaje = str(ex), estado = fixture)

class GenerarEliminacion(graphene.Mutation):
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        try:
            fase = fixture.eliminacion()
            return GenerarEliminacion(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return GenerarEliminacion(ok = False, mensaje = str(ex), estado = fixture)

class GenerarFinal(graphene.Mutation):
    class Input:
        jugadores = graphene.NonNull(graphene.Int)
        
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        jugadores = kwargs.get('jugadores')
        try:
            fase = fixture.final(jugadores)
            return GenerarFinal(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return GenerarFinal(ok = False, mensaje = str(ex), estado = fixture)

class GenerarAdHoc(graphene.Mutation):
    class Input:
        robots = graphene.List(graphene.String)
        
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        robots = kwargs.get('robots')
        try:
            fase = fixture.adhoc(robots)
            return GenerarFinal(ok = True, mensaje = "Fase creada", fase = fase, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return GenerarFinal(ok = False, mensaje = str(ex), estado = fixture)

class GenerarRonda(graphene.Mutation):
    class Input:
        grupo = graphene.NonNull(graphene.Int)
        tct = graphene.NonNull(graphene.Boolean)
        esc = graphene.NonNull(graphene.Boolean)
        allow_none = graphene.NonNull(graphene.Boolean)
        shuffle = graphene.NonNull(graphene.Boolean)
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    ronda = graphene.Field(Ronda)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        ngrupo = kwargs.get('grupo')
        tct = kwargs.get('tct')
        esc = kwargs.get('esc')
        allow_none = kwargs.get('allow_none')
        shuffle = kwargs.get('shuffle')
        try:
            ronda = fixture.generar_ronda(ngrupo, tct, esc, allow_none, shuffle)
            return GenerarRonda(ok = True, mensaje = "Ronda creada", ronda = ronda, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
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
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        key = kwargs.get('key')
        nencuentro = kwargs.get('encuentro')
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
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        key = kwargs.get('key')
        nencuentro = kwargs.get('encuentro')
        try:
            robot = fixture.get_robot_por_key(key)
            encuentro = fixture.quitar_ganador(robot, nencuentro)
            return AgregarGanador(ok = True, mensaje = "Robot no declarado ganador", encuentro = encuentro, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return AgregarGanador(ok = False, mensaje = str(ex), estado = fixture)

class AgregarAdversario(graphene.Mutation):
    class Input:
        encuentro = graphene.NonNull(graphene.Int)
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    encuentro = graphene.Field(lambda: Encuentro)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        nencuentro = kwargs.get('encuentro')
        try:
            encuentro = fixture.agregar_adversario(nencuentro)
            return AgregarGanador(ok = True, mensaje = "Encuentro resuelto con nuevo adversario", encuentro = encuentro, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return AgregarGanador(ok = False, mensaje = str(ex), estado = fixture)

class ArmarFinal(graphene.Mutation):
    class Input:
        fase = graphene.NonNull(graphene.Int)
    
    ok = graphene.Boolean()
    mensaje = graphene.String()
    fase = graphene.Field(lambda: Fase)
    estado = graphene.Field(Estado)
    
    @staticmethod
    def mutate(root, info, *args, **kwargs):
        context = info.context
        fixture = context["fixture"]
        nfase = kwargs.get('fase')
        try:
            fase = fixture.armar_final(nfase)
            return ArmarFinal(ok = True, mensaje = "Final completado con robots", fase = fase, estado = fixture)
        except Exception as ex:
            traceback.print_exc()
            return ArmarFinal(ok = False, mensaje = str(ex), estado = fixture)

class Mutations(graphene.ObjectType):
    generar_clasificacion = GenerarClasificacion.Field()
    generar_eliminacion = GenerarEliminacion.Field()
    generar_final = GenerarFinal.Field()
    generar_adhoc = GenerarAdHoc.Field()
    generar_ronda = GenerarRonda.Field()
    agregar_ganador = AgregarGanador.Field()
    quitar_ganador = QuitarGanador.Field()
    agregar_adversario = AgregarAdversario.Field()
    armar_final = ArmarFinal.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
