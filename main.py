from flask import Flask, render_template
from flask_graphql import GraphQLView

from server import Fixture, schema

ROBOTS = [
    ("Ultron", "Los Avengers","Nick Fury"),
    ("Wall-e","Pixar","Sr. Disney"),
    ("EVA","Pixar","Sr. Disney"),
    ("Rodney","Robots","Sr. Ewan McGregor"),
    ("Sony","R&H Mecanicos","Dt. Spooner"),
    ("Robocop","O.C.P.","Bob Morthon"),
    ("ED 209","O.C.P.","Bob Morthon"),
    ("Johnny 5","Cortocircuito","Ally Sheedy"),
    ("T-800","Cyberdyne Systems","Jhon Connor"),
    ("T-1000","Cyberdyne Systems","Arnie"),
    ("R2-D2","La Republica","Obiwan Kenobi"),
    ("3-CPO","La Republica","Anakin Skywalker"),
    ("BB-8","La Republica","Poe Dameron"),
    ("Roy Batty","Blade Runner","Roy"),
    ("HAL 9000","Discovery Uno","David Bowman"),
    ("Ash","Nostromo","Ellen Ripley"),
    ("Optimus Prime","Transformers","Ellen Ripley"),
    ("David Swinton","IA","Ellen Ripley"),
    ("Teddy","IA","Haley Joel Osment"),
    ("Centinelas","Matrix","Neo"),
    ("Bender", "Futurama", "Philip J. Fry")
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