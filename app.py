from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from flask_serialize import FlaskSerializeMixin
from flask_mysqldb import MySQL
from flask_restful import Resource, Api, reqparse
from settings import config

app = Flask(__name__)

app.config['MYSQL_HOST'] = config['db_host']
app.config['MYSQL_USER'] = config['db_user']
app.config['MYSQL_PASSWORD'] = config['db_password']
app.config['MYSQL_DB'] = config['db_name']

db = MySQL(app)

api = Api(app)

def parse_user_information():

    parser = reqparse.RequestParser()

    parser.add_argument('user_id', type=str)
    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('date_of_birth', type=str)
    parser.add_argument('address', type=str)
    parser.add_argument('phone_number', type=int)
    parser.add_argument('gender', type=str)
    parser.add_argument('title', type=str)

    return parser


class UsersAction(Resource):
    
    def post(self):
        parse = parse_user_information()
        data = parse.parse_args()

        cursor = db.connection.cursor()
        query = "INSERT INTO `tcm`.users(user_id, first_name, last_name, date_of_birth, address, phone_number, gender, title) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (data['user_id'], data['first_name'], data['last_name'], data['date_of_birth'], data['address'], data['phone_number'], data['gender'], data['title'],))
        db.connection.commit()

        return {'message': 'User created!'}, 200
    
    def get(self):
        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.users;"
        cursor.execute(query)

        result = cursor.fetchall()
        print(jsonify(result))

        return {'message': 'Successfully retrieve all users!'}, 200

class SingleUserAction(Resource):
    def get(self, user_id):

        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.users WHERE user_id=%s;"
        cursor.execute(query, (str(user_id),))

        result = cursor.fetchone()
        print(result)

        return {'message': 'Successfully get information of a user'}, 200

class DoctorAction(Resource):
    def get(self, user_id):
        cursor = db.connection.cursor()
        pass

class PatientAction(Resource):
    def get(self, user_id):
        pass

class AssistantDoctorAction(Resource):
    def get(self, user_id):
        pass

# class PatientDiagnosis(Resource):
#     def get(self, user_id):
#         pass


api.add_resource(UsersAction, '/api/v1/users')
api.add_resource(SingleUserAction, '/api/v1/users/<user_id>')
api.add_resource(DoctorAction, '/api/v1/doctor/<user_id>')
api.add_resource(AssistantDoctorAction, '/api/v1/assistant_doctor/<user_id>')
api.add_resource(PatientAction, '/api/v1/patients/<user_id>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)