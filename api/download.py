from flask_restful import Resource
from flask import send_from_directory

class DownloadEndpoint(Resource):
    def get(self, filename):
        return send_from_directory(directory='simulations', filename=filename)