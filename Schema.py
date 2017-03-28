from graphql import (
    graphql,
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLList,
    GraphQLNonNull,
    GraphQLString
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

queryType = GraphQLObjectType(
    name='Query',
    fields = {
      'robots': GraphQLField(
        GraphQLList(robotType),
        description='Los robots inscriptos en la competencia.',
        resolver=lambda root, *_: fixture.robots,
      )
    }
  )

schema = GraphQLSchema(
  queryType
)