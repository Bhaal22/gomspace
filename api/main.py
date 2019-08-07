from flask import Flask
from flask_restful import Api, Resource, reqparse
from api.simulator import SimulatorEndpoint
from api.download import DownloadEndpoint

app = Flask('Gomspace Simulator')
api = Api(app)

api.add_resource(SimulatorEndpoint, '/simulator/<int:steps>')
api.add_resource(DownloadEndpoint, '/downloads/<string:filename>')

app.run(debug=True)