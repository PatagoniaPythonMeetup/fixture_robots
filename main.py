import json
from flask import Flask, render_template
from flask_graphql import GraphQLView
from flask_cors import CORS

from faker import Factory

from server import Fixture, schema, Encuentro, Ronda

fake = Factory.create()
FIXTURE = Fixture()
with open("./datos/robots.json", "r") as f:
    for robot in json.loads(f.read()):
        FIXTURE.inscribir_robot(*robot)

app = Flask(__name__)
CORS(app)

app.add_url_rule('/fixture', view_func = GraphQLView.as_view('fixture', 
    schema=schema, 
    context={"fixture": FIXTURE},
    graphiql=True))

@app.route('/')
def index(): 
    return render_template("index.html", robots = len(FIXTURE.robots))

@app.route('/store')
def dumps():
    with open("./datos/fixture.json", "w") as f:
        f.write(json.dumps(FIXTURE.to_dict()))
    return render_template("index.html", robots = len(FIXTURE.robots))

@app.route('/restore')
def loads():
    with open("./datos/fixture.json", "r") as f:
        FIXTURE.from_dict(json.loads(f.read()))
    return render_template("index.html", robots = len(FIXTURE.robots))

@app.route('/clean')
def clean():
    FIXTURE.limpiar()
    return render_template("index.html", robots = len(FIXTURE.robots))

@app.route('/faker/<num>')
def faker(num):
    for _ in range(int(num)):
        FIXTURE.inscribir_robot(fake.name(), fake.name(), fake.name())
    return render_template("index.html", robots = len(FIXTURE.robots))

def main():
    app.run()

if __name__ == '__main__':
    main()