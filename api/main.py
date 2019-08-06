from flask import Flask
from flask_restful import Api, Resource, reqparse
from api.simulator import SimulatorEndpoint

app = Flask('Gomspace Simulator')
api = Api(app)

api.add_resource(SimulatorEndpoint, '/simulator/')
app.run(debug=True)