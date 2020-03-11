from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class LedApi(Resource):
    def get(self, led_no):
        return {
            'type':'GET',
            'led_no':led_no
            }
    def post(self, led_no):
        return {'type':'POST'}
    def put(self, led_no):
        return {'type':'PUT'}
    def delete(self, led_no):
        return {'type':'DELETE'}

api.add_resource(LedApi, '/rest/v2/leds/<int:led_no>')

if __name__ == '__main__' :
    app.run(debug=True)
