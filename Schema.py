from graphql import (
    graphql,
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLList,
    GraphQLNonNull,
    GraphQLString,
    GraphQLInt,
    GraphQLArgument
)

robotType = GraphQLObjectType(
    'Robot',
    description='Un robot.',
    fields=lambda: {
        'nombre': GraphQLField(
            GraphQLNonNull(GraphQLString),
            description='El nombre del robot.',
        ),
        'escuela': GraphQLField(
            GraphQLNonNull(GraphQLString),
            description='El nombre de la escuela manufacturera.',
        ),
        'encargado': GraphQLField(
            GraphQLNonNull(GraphQLString),
            description='El nombre del encargado por escuela.',
        )
    }
)

encuentroType = GraphQLObjectType(
    'Encuentro',
    description='Dos robots entran solo uno sale.',
    fields=lambda: {
        'robot_1': GraphQLField(
            GraphQLNonNull(robotType),
            description='El primer robot.',
        ),
        'robot_2': GraphQLField(
            GraphQLNonNull(robotType),
            description='El segundo robot.',
        ),
        'ganadas': GraphQLField(
            GraphQLList(robotType),
            description='Listado de enfrentamientos ganados entre el primero y el segundo robot.',
        )
    }
)

rondaType = GraphQLObjectType(
    'Ronda',
    description='Una vuelta completa de competencias.',
    fields=lambda: {
        'numero': GraphQLField(
            GraphQLNonNull(GraphQLInt),
            description='Numero de la ronda con base 0.',
        ),
        'encuentros': GraphQLField(
            GraphQLList(encuentroType),
            description='Los encuentros de cada ronda.',
            resolver=lambda ronda, args, *_: ronda.encuentros,
        ),
        'promovidos': GraphQLField(
            GraphQLList(robotType),
            description='Los robots promovidos de la ronda.',
            resolver=lambda ronda, args, *_: ronda.promovidos,
        )
    }
)

def schema(fixture):
    queryType = GraphQLObjectType(
        name='Query',
        fields = {
        'robots': GraphQLField(
            GraphQLList(robotType),
            description='Los robots inscriptos en la competencia.',
            resolver=lambda root, *_: fixture.robots,
        ),
        'rondas': GraphQLField(
            GraphQLList(rondaType),
            description='Las rondas de la competencia.',
            resolver=lambda root, *_: fixture.rondas,
        )
        }
    )
    return GraphQLSchema(queryType)