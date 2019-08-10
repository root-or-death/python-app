from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'app': 'app2'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
