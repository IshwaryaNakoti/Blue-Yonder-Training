from flask import Flask, request, redirect, jsonify
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60))
    password = db.Column(db.String(500))
    mobile_number = db.Column(db.String(300))

    def user_serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "password": self.password,
            "mobile_number":self.mobile_number
        }
    def __str__(self):
        return self.name + self.email + str(self.mobile_number)

@app.route('/create', methods = ['POST'])
def create_user():
    if request.method == 'POST':
        u = request.get_json()

        user = User(
            name = u.get('name'),
            email = u.get('email'),
            password = u.get('password'),
            mobile_number = u.get('mobile_number')
        )
        db.session.add(user)
        db.session.commit()

        message = {
            'data' : 'Record inserted succesfully'
        }
        return jsonify(message)

@app.route('/list', methods =[ 'GET'])
def list_user():
    user = User.query.all()
    listUser = []
    for u in user:
        listUser.append(u.user_serialize())
    return jsonify(listUser)
@app.route('/delete_user', methods = ['DELETE'])
def delete_user():
    if request.method == 'DELETE':
        u = request.get_json()
        user_id = u.get('id')
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            message = {"data" : "Record deleted successfully"}
        else:
            message = {"data" : "User not found"}
        return jsonify(message)

@app.route('/update_user', methods = ['PUT'])
def update_user():
    if request.method == 'PUT':
        u = request.get_json()
        user_id = u.get('id')
        user = User.query.get(user_id)
        if user:
            user.name = u.get('name', user.name)
            user.email = u.get('email', user.email)
            user.password = u.get('password', user.password)
            user.mobile_number = u.get('mobile_number', user.mobile_number)
            db.session.commit()
            message = {
                "data" : "Record updated succesfully"
            }
        else:
            message = {
                "data" : "User not found"
            }
        return jsonify(message)

with app.app_context():
    db.create_all()
app.run(debug=True)