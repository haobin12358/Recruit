from flask import Flask
import flask_restful
from apis.Users import Users


app = Flask(__name__)
api = flask_restful.Api(app)

api.add_resource(Users,"/users/<string:name>")

if __name__ == '__main__':
    app.run('0.0.0.0',7443,debug=True)