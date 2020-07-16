from flask_restful import Resource, reqparse

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('date_of_birth', type=str)
    parser.add_argument('address', type=str)
    parser.add_argument('phone_number', type=str)
    parser.add_argument('gender', type=str)
    parser.add_argument('title', type=str)
    
    def post(self):
        pass


class Doctor(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('')
    def get(self, user_id):
        pass

class Patient(Resource):
    def get(self, user_id):
        pass

class AssistantDoctor(Resource):
    def get(self, user_id):
        pass