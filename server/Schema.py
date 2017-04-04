import graphene
from graphene import resolve_only_args

class Robot(graphene.ObjectType):
    nombre = graphene.String()
    escuela = graphene.String()
    encargado = graphene.String()

class Encuentro(graphene.ObjectType):
    numero = graphene.Int()
    robot_1 = graphene.Field(Robot)
    robot_2 = graphene.Field(Robot)
    ganadas = graphene.List(Robot)

class Ronda(graphene.ObjectType):
    numero = graphene.Int()
    encuentros = graphene.List(Encuentro)
    promovidos = graphene.List(Robot)

class Fixture(graphene.ObjectType):
    numero = graphene.Int()
    encuentros = graphene.List(Encuentro)
    promovidos = graphene.List(Robot)

class CrearRonda(graphene.Mutation):
    ok = graphene.Boolean()
    ronda = graphene.Field(lambda: Ronda)

    @staticmethod
    def mutate(root, args, context, info):
        ronda = context["fixture"].ronda()
        ok = True
        return CrearRonda(ronda=ronda, ok=ok)

class Query(graphene.ObjectType):
    robots = graphene.List(Robot)
    rondas = graphene.List(Ronda)

    def resolve_robots(self, args, context, info):
        return context["fixture"].robots

    def resolve_rondas(self, args, context, info):
        return context["fixture"].rondas

class Mutations(graphene.ObjectType):
    crear_ronda = CrearRonda.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)