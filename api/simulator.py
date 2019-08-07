import uuid
import os

from flask_restful import Resource
from src.simulator import Simulator

class SimulatorEndpoint(Resource):
    def put(self, steps):
        simulator = Simulator()

        simulator.run(steps)

        folder = 'simulations'
        filename = 'simulation-%d-%s' % (steps, uuid.uuid4())
        simulator.export_grid(os.path.join(folder, filename))

        return filename