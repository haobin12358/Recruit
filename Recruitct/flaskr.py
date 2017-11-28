from flask import Flask
import flask_restful
from apis.Users import Login,Resgiter,Test


app = Flask(__name__)
api = flask_restful.Api(app)

api.add_resource(Login,"/login")
api.add_resource(Resgiter,"/resgiter")
api.add_resource(Test,"/test")

if __name__ == '__main__':
    app.run('0.0.0.0',7443,debug=True)