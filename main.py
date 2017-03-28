from flask import Flask
from flask_graphql import GraphQLView
#http://www.aropupu.fi/bracket/

from Schema import schema

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

def main():
    app.run()

if __name__ == '__main__':
    main()