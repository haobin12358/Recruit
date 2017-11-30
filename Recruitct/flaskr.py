from flask import Flask
import flask_restful
from apis.Users import Users
from apis.Works import Works
from apis.Items import Items
from apis.Parteners import Parteners
from apis.Compony import Compony


app = Flask(__name__)
api = flask_restful.Api(app)

api.add_resource(Users,"/users/<string:name>")
api.add_resource(Works,"/works/<string:work>")
api.add_resource(Items,"/items/<string:item>")
api.add_resource(Parteners,"/parteners/<string:partener>")
api.add_resource(Compony,"/compony/<string:compony>")

if __name__ == '__main__':
    app.run('0.0.0.0',7443,debug=True)