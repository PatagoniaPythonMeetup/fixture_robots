import os
import sys

HOST = os.environ.get('HOST', '127.0.0.1')
try:
    PORT = int(os.environ.get('PORT', 5000))
except Exception as e:
    sys.stderr.write("Error {} getting PORT. Setting to 5000".format(e))
    PORT = 5000

DEBUG = True if os.environ.get('DEBUG') else False

import json
from flask import Flask, render_template, redirect
from flask_graphql import GraphQLView
from flask_cors import CORS

from faker import Factory

from server import Fixture, schema, Encuentro, Ronda, Robot_scrapper

fake = Factory.create()

FIXTURE = Fixture()
with open("./datos/robots.json", "r") as f:
    for robot in json.loads(f.read()):
        FIXTURE.inscribir_robot(*robot)

SCRAPPER = Robot_scrapper(True)
SCRAPPER.scrap_file()

app = Flask(__name__)
CORS(app)

app.add_url_rule('/fixture', view_func = GraphQLView.as_view('fixture', 
    schema=schema, 
    get_context= lambda *args, **kwargs: {"fixture": FIXTURE},
    graphiql=True))

@app.route('/')
def index(): 
    return render_template("index.html", robots = len(FIXTURE.robots))

@app.route('/scrapper/<categoria>')
def scrapper(categoria):
    equipos = SCRAPPER.get_equipos()
    equipos = [equipo for equipo in equipos if equipo.categoria.lower().startswith(categoria)]
    FIXTURE.limpiar()
    for equipo in equipos:
        FIXTURE.inscribir_equipo(equipo)
    return redirect("/")

@app.route('/store/<categoria>')
def dumps(categoria):
    with open(f"./datos/{categoria}.json", "w") as f:
        f.write(json.dumps(FIXTURE.to_dict()))
    return redirect("/")

@app.route('/restore/<categoria>')
def loads(categoria):
    with open(f"./datos/{categoria}.json", "r") as f:
        FIXTURE.from_dict(json.loads(f.read()))
    return redirect("/")

@app.route('/clean')
def clean():
    FIXTURE.limpiar()
    return redirect("/")

@app.route('/faker/<num>')
def faker(num):
    for _ in range(int(num)):
        FIXTURE.inscribir_robot(fake.name(), fake.name(), fake.name())
    return redirect("/")

def main():
    app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == '__main__':
    main()