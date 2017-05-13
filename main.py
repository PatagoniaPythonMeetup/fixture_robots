import json
from flask import Flask, render_template
from flask_graphql import GraphQLView
from flask_cors import CORS

from server import Fixture, schema, Encuentro, Ronda

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
    return render_template("index.html")

@app.route('/store')
def loads():
    with open("./datos/fixture.json", "r") as f:
        FIXTURE.from_dict(json.loads(f.read()))
    return render_template("index.html")

@app.route('/restore')
def dumps():
    with open("./datos/fixture.json", "w") as f:
        f.write(json.dumps(FIXTURE.to_dict()))
    return render_template("index.html")

def main():
    app.run()

if __name__ == '__main__':
    main()