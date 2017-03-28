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

from Fixture import Fixture
from Robot import Robot

robots = [
    Robot("Ultron", "Los Avengers","Nick Fury"),
    Robot("Wall-e","Pixar","Sr. Disney"),
    Robot("Sony","R&H Mecanicos","Dt. Spooner"),
    Robot("Robocop","O.C.P.","Bob Morthon"),
    Robot("Terminator","Skynet","Jhon Connor"),
    Robot("R2-D2","La Republica","Obiwan Kenobi"),
    Robot("3-CPO","La Republica","Anakin Skywalker"),
    Robot("BB-8","La Republica","Poe Dameron")
]

fixture = Fixture(robots)
ronda = fixture.ronda()

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
        )
    }
)

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

schema = GraphQLSchema(
  queryType
)