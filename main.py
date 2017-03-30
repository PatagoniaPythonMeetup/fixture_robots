from flask import Flask
from flask_graphql import GraphQLView
#http://www.aropupu.fi/bracket/

from Fixture import Fixture
from Robot import Robot
from Schema import schema

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

app = Flask(__name__)

app.add_url_rule('/graphql', view_func = GraphQLView.as_view('graphql', 
    schema=schema, 
    context={"fixture": fixture},
    graphiql=True))

def main():
    app.run()

if __name__ == '__main__':
    main()