import json
from flask import Flask, render_template
from flask_graphql import GraphQLView
from flask_cors import CORS

from server import Fixture, schema, Encuentro, Ronda

FIXTURE = Fixture()

app = Flask(__name__)
CORS(app)

app.add_url_rule('/fixture', view_func = GraphQLView.as_view('fixture', 
    schema=schema, 
    context={"fixture": FIXTURE},
    graphiql=True))

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/loads')
def loads():
    with open("./fixture.json", "r") as f:
        FIXTURE.from_dict(json.loads(f.read()))
    return render_template("index.html")

@app.route('/dumps')
def dumps():
    with open("./fixture.json", "w") as f:
        f.write(json.dumps(FIXTURE.to_dict()))
    return render_template("index.html")

def main():
    app.run()

if __name__ == '__main__':
    main()