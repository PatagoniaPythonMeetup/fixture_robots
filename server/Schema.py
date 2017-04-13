import graphene
from graphene import resolve_only_args

class Robot(graphene.ObjectType):
    nombre = graphene.String()
    escuela = graphene.String()
    encargado = graphene.String()
    score = graphene.Int()

    def resolve_puntaje(self, args, context, info):
        return context["fixture"].score(self)

class Encuentro(graphene.ObjectType):
    numero = graphene.Int()
    vuelta = graphene.Int()
    robots = graphene.List(Robot)
    resultados = graphene.List(graphene.Int)

    def resolve_vuelta(self, args, context, info):
        return self.vuelta()

    def resolve_robots(self, args, context, info):
        return [self.robot_1, self.robot_2]

    def resolve_resultados(self, args, context, info):
        return self.resultados()


class Ronda(graphene.ObjectType):
    numero = graphene.Int()
    vuelta = graphene.Int()
    encuentros = graphene.List(Encuentro)
    promovidos = graphene.List(Robot)

    def resolve_vuelta(self, args, context, info):
        return self.vuelta()

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