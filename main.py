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

SCRAPPER = Robot_scrapper()

app = Flask(__name__)
CORS(app)

app.add_url_rule('/fixture', view_func = GraphQLView.as_view('fixture', 
    schema=schema, 
    context={"fixture": FIXTURE},
    graphiql=True))

@app.route('/')
def index(): 
    return render_template("index.html", robots = len(FIXTURE.robots))

@app.route('/robocomp/seguidor')
def robocomp_seguidor():
    equipos = SCRAPPER.get_equipos()
    equipos = [equipo for equipo in equipos if equipo.categoria.startswith("Seguidor")]
    FIXTURE.limpiar()
    for equipo in equipos:
        FIXTURE.inscribir_equipo(equipo)
    return redirect("/")

@app.route('/robocomp/sumo')
def robocomp_sumo():
    equipos = SCRAPPER.get_equipos()
    equipos = [equipo for equipo in equipos if equipo.categoria.startswith("Sumo")]
    FIXTURE.limpiar()
    for equipo in equipos:
        FIXTURE.inscribir_equipo(equipo)
    return redirect("/")
    
@app.route('/robocomp/minisumo')
def robocomp_minisumo():
    equipos = SCRAPPER.get_equipos()
    equipos = [equipo for equipo in equipos if equipo.categoria.startswith("Mini-Sumo")]
    FIXTURE.limpiar()
    for equipo in equipos:
        FIXTURE.inscribir_equipo(equipo)
    return redirect("/")

@app.route('/robocomp/futbol')
def robocomp_futbol():
    equipos = SCRAPPER.get_equipos()
    equipos = [equipo for equipo in equipos if equipo.categoria.startswith("Fútbol")]
    FIXTURE.limpiar()
    for equipo in equipos:
        FIXTURE.inscribir_equipo(equipo)
    return redirect("/")

@app.route('/store')
def dumps():
    with open("./datos/fixture.json", "w") as f:
        f.write(json.dumps(FIXTURE.to_dict()))
    return redirect("/")

@app.route('/restore')
def loads():
    with open("./datos/fixture.json", "r") as f:
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
    app.run()

if __name__ == '__main__':
    main()