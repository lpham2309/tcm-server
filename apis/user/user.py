from flask_restful import Resource, reqparse
from .. import *
from flask import jsonify

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

def parse_update_user_information():
    
    parser = reqparse.RequestParser()

    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('date_of_birth', type=str)
    parser.add_argument('address', type=str)
    parser.add_argument('phone_number', type=int)

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

        try:
            result = cursor.fetchall()
        except Exception:
            return {
                'error': 'No users found'
            }, 400
        return {'message': 'Successfully retrieve all users!'}, 200

class SingleUserAction(Resource):
    def get(self, user_id):

        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.users WHERE user_id=%s;"
        cursor.execute(query, (str(user_id),))

        try:
            result = cursor.fetchone()
        except Exception:
            return {
                'error': 'Unable to retrieve user'
            }, 400

        # return {'message': 'Successfully get information of a user'}, 200
        return jsonify(result)
    
    def put(self, user_id):
        parse = parse_update_user_information()
        data = parse.parse_args()

        cursor = db.connection.cursor()
        query = "UPDATE `tcm`.users SET \
            first_name=%s, last_name=%s, date_of_birth=%s, \
            address=%s, phone_number=%s WHERE user_id=%s;"
        cursor.execute(query, (
            data['first_name'], data['last_name'], data['date_of_birth'],
            data['address'], data['phone_number'], user_id,))
        
        db.connection.commit()
        return {
            'message': 'Successfully updated current user!'
        }

# Note: these classes below will need refactoring
class DoctorAction(Resource):
    def get(self, user_id):

        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.doctors WHERE user_id=%s AND role_name='doctor';"
        cursor.execute(query, (str(user_id),))

        try:
            result = cursor.fetchone()
        except Exception:
            return {
                'error': 'No doctor exists with current ID'
            }, 400
        return {
            'message': 'Successfully retrieve current doctor'
        }, 200
class PatientAction(Resource):
    def get(self, user_id):
        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.patients WHERE user_id=%s AND role_name='patient';"
        cursor.execute(query, (str(user_id),))

        try:
            result = cursor.fetchone()
        except Exception:
            return {
                'error': 'No patient exists with current ID'
            }, 400
        return {
            'message': 'Successfully retrieve current patients'
        }, 200

class AssistantDoctorAction(Resource):
    def get(self, user_id):
        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.assistant_doctors WHERE user_id=%s AND role_name='assistant_doctor';"
        cursor.execute(query, (str(user_id),))

        try:
            result = cursor.fetchone()
        except Exception:
            return {
                'error': 'No assistant doctor exists with current ID'
            }, 400
        return {
            'message': 'Successfully retrieve current assistant doctor'
        }, 200