import json
from flask import Flask, render_template
from flask_graphql import GraphQLView

from server import Fixture, schema, Encuentro, Ronda

with open("./fixture.json", "r") as f:
    data = json.loads(f.read())
    fixture = Fixture.from_json(data)

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