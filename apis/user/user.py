from flask_restful import Resource, reqparse
from .. import *

def parse_user_information():

    parser = reqparse.RequestParser()

    parser.add_argument('user_id', type=str, required=True)
    parser.add_argument('first_name', type=str, required=True)
    parser.add_argument('last_name', type=str, required=True)
    parser.add_argument('date_of_birth', type=str, required=True)
    parser.add_argument('address', type=str, required=True)
    parser.add_argument('phone_number', type=int, required=True)
    parser.add_argument('gender', type=str, required=True)
    parser.add_argument('role_name', type=str, required=True)

    return parser
class UsersAction(Resource):
    
    def post(self):
        parse = parse_user_information()
        data = parse.parse_args()

        cursor = db.connection.cursor()
        query = "INSERT INTO `tcm`.users(user_id, first_name, last_name, date_of_birth, address, phone_number, gender, role_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (data['user_id'], data['first_name'], data['last_name'], data['date_of_birth'], data['address'], data['phone_number'], data['gender'], data['role_name'],))
        db.connection.commit()

        return {'message': 'User created!'}, 200
    
    def get(self):
        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.users;"
        cursor.execute(query)

        result = cursor.fetchall()

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