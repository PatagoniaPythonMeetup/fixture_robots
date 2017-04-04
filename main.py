from flask import Flask, render_template
from flask_graphql import GraphQLView
#http://www.aropupu.fi/bracket/

from server import Fixture, schema

ROBOTS = [
    ("Ultron", "Los Avengers","Nick Fury"),
    ("Wall-e","Pixar","Sr. Disney"),
    ("Sony","R&H Mecanicos","Dt. Spooner"),
    ("Robocop","O.C.P.","Bob Morthon"),
    ("Terminator","Skynet","Jhon Connor"),
    ("R2-D2","La Republica","Obiwan Kenobi"),
    ("3-CPO","La Republica","Anakin Skywalker"),
    ("BB-8","La Republica","Poe Dameron")
]

fixture = Fixture()
for robot in ROBOTS:
    fixture.inscribir(*robot)

app = Flask(__name__)

app.add_url_rule('/fixture', view_func = GraphQLView.as_view('fixture', 
    schema=schema, 
    context={"fixture": fixture},
    graphiql=True))

@app.route('/')
def index(): 
    return render_template("index.html")

def main():
    app.run()

if __name__ == '__main__':
    main()