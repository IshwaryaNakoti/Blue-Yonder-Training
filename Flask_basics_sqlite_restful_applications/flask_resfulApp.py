from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


class Hello(Resource):
    def get(self):
        return jsonify({"message": "Hello world"})
    
    def post(self):
        data = request.get_json()
        return {"data" : data}, 201
    
class Square(Resource):
    def get(self, num):
        return {"Square": num ** 2}, 201
    
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')

app.run(debug=True)
