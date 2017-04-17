import graphene
from graphene import resolve_only_args

class Robot(graphene.ObjectType):
    nombre = graphene.String()
    escuela = graphene.String()
    encargado = graphene.String()
    score = graphene.List(graphene.Int)

    def resolve_score(self, args, context, info):
        return context["fixture"].score(self)

class Encuentro(graphene.ObjectType):
    numero = graphene.Int()
    jugadas = graphene.Int()
    robots = graphene.List(Robot)
    finalizado = graphene.Boolean()

    def resolve_jugadas(self, args, context, info):
        return self.jugadas()

    def resolve_robots(self, args, context, info):
        return [self.robot_1, self.robot_2]


class Ronda(graphene.ObjectType):
    numero = graphene.Int()
    vuelta = graphene.Int()
    jugadas = graphene.Int()
    encuentros = graphene.List(Encuentro)
    promovidos = graphene.List(Robot)
    finalizada = graphene.Boolean()

    def resolve_vuelta(self, args, context, info):
        return self.vuelta()
    
    def resolve_jugadas(self, args, context, info):
        return self.jugadas()

    def resolve_finalizada(self, args, context, info):
        return self.finalizada()

class Fixture(graphene.ObjectType):
    numero = graphene.Int()
    encuentros = graphene.List(Encuentro)
    promovidos = graphene.List(Robot)
    finalizado = graphene.Boolean()

class GenerarRonda(graphene.Mutation):
    ok = graphene.Boolean()
    ronda = graphene.Field(lambda: Ronda)

    @staticmethod
    def mutate(root, args, context, info):
        ronda = context["fixture"].generar_ronda()
        ok = True
        return GenerarRonda(ronda=ronda, ok=ok)

class GanaRobot(graphene.Mutation):
    class Input:
        nombre = graphene.String()
    
    ok = graphene.Boolean()
    
    @staticmethod
    def mutate(root, args, context, info):
        nombre = args.get('nombre')
        robot = context["fixture"].get_robot_por_nombre(nombre)
        context["fixture"].gano(robot)
        ok = True
        return GanaRobot(ok=ok)

class Query(graphene.ObjectType):
    robots = graphene.List(Robot)
    rondas = graphene.List(Ronda)

    def resolve_robots(self, args, context, info):
        return context["fixture"].robots

    def resolve_rondas(self, args, context, info):
        return context["fixture"].rondas

class Mutations(graphene.ObjectType):
    generar_ronda = GenerarRonda.Field()
    gana_robot = GanaRobot.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)