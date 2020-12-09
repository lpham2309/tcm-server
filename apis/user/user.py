from flask_restful import Resource, reqparse
from .. import *
from flask import jsonify
from tcm_project.models.users import Users, Doctors


def parse_user_information():

    parser = reqparse.RequestParser()

    parser.add_argument('user_id', type=int)
    parser.add_argument('first_name', type=str, required=True)
    parser.add_argument('last_name', type=str, required=True)
    parser.add_argument('date_of_birth', type=str, required=True)
    parser.add_argument('address', type=str, required=True)
    parser.add_argument('phone_number', type=str, required=True)
    parser.add_argument('gender', type=str, required=True)
    parser.add_argument('role_name', type=str, required=True)
    parser.add_argument('is_active', type=int)
    return parser


def parse_update_user_information():

    parser = reqparse.RequestParser()

    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('date_of_birth', type=str)
    parser.add_argument('address', type=str)
    parser.add_argument('phone_number', type=int)

    return parser


def parse_user_active():
    parser = reqparse.RequestParser()
    parser.add_argument('is_active', type=int)

    return parser


class UsersAction(Resource):

    def post(self):
        parse = parse_user_information()
        data = parse.parse_args()

        # cursor = db.connection.cursor()
        # query = "INSERT INTO `tcm`.users(user_id, first_name, last_name, date_of_birth, address, phone_number, gender, role_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        # cursor.execute(query, (data['user_id'], data['first_name'], data['last_name'], data['date_of_birth'],
        #                        data['address'], data['phone_number'], data['gender'], data['role_name'],))

        user = Users(data['user_id'], data['first_name'], data['last_name'], data['date_of_birth'],
                     data['address'], data['phone_number'], data['gender'], data['role_name'], data['is_active'])

        db.session.add(user)
        db.session.commit()

        return {'message': 'User created!'}, 200

    def get(self):
        # cursor = db.connection.cursor()
        # query = "SELECT * FROM `tcm`.users;"
        # cursor.execute(query)

        try:
            results = []
            users = Users.query.limit(20).all()

            for user in users:
                results.append(user.to_json2())
            return results
        except Exception:
            return {
                'error': 'No users found'
            }, 400
        return {'message': 'Successfully retrieve all users!'}, 200


class SingleUserAction(Resource):
    def get(self, user_id):

        try:
            result = Users.query.get(user_id)
        except Exception:
            return {
                'error': 'Unable to retrieve user'
            }, 400

        # return {'message': 'Successfully get information of a user'}, 200
        return jsonify(result.to_json2())

    def put(self, user_id):
        parse = parse_update_user_information()
        data = parse.parse_args()

        # cursor = db.connection.cursor()
        # query = "UPDATE `tcm`.users SET \
        #     first_name=%s, last_name=%s, date_of_birth=%s, \
        #     address=%s, phone_number=%s WHERE user_id=%s;"
        # cursor.execute(query, (
        #     data['first_name'], data['last_name'], data['date_of_birth'],
        #     data['address'], data['phone_number'], user_id,))

        user = Users.query.get(user_id)
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.date_of_birth = data['date_of_birth']
        user.address = data['address']
        user.phone_number = data['phone_number']

        db.session.commit()
        return {
            'message': 'Successfully updated current user!'
        }, 200

    def post(self, user_id):
        parse = parse_user_active()
        data = parse.parse_args()

        # cursor = db.connection.cursor()

        # query = "UPDATE `tcm`.users SET is_active=%s WHERE user_id=%s;"
        # cursor.execute(query, (data['is_active'], user_id,))

        user = Users.query.get(user_id)
        user.is_active = data['is_active']

        db.session.commit()
        return {
            'message': 'This user has been archived!'
        }


class DoctorAction(Resource):
    def get(self, user_id):

        # cursor = db.connection.cursor()
        # query = "SELECT * FROM `tcm`.doctors WHERE user_id=%s AND role_name='doctor';"
        # cursor.execute(query, (str(user_id),))

        try:
            current_user = Users.query.get(user_id)
            if current_user.is_active and current_user.role_name == 'doctor':
                result = current_user.get_user_information()
        except Exception:
            return {
                'error': 'No doctor exists with current ID'
            }, 400
        return result, 200


class PatientAction(Resource):
    def get(self, user_id):
        # cursor = db.connection.cursor()
        # query = "SELECT * FROM `tcm`.patients WHERE user_id=%s AND role_name='patient';"
        # cursor.execute(query, (str(user_id),))

        try:
            current_user = Users.query.get(user_id)
            if current_user.is_active and current_user.role_name == 'patient':
                result = current_user.get_user_information()
        except Exception:
            return {
                'error': 'No patient exists with current ID'
            }, 400
        return result, 200


class AssistantDoctorAction(Resource):
    def get(self, user_id):
        # cursor = db.connection.cursor()
        # query = "SELECT * FROM `tcm`.assistant_doctors WHERE user_id=%s AND role_name='assistant_doctor';"
        # cursor.execute(query, (str(user_id),))

        try:
            current_user = Users.query.get(user_id)
            if current_user.is_active and current_user.role_name == 'assistant_doctor':
                result = current_user.get_user_information()
        except Exception:
            return {
                'error': 'No assistant doctor exists with current ID'
            }, 400
        return result, 200
