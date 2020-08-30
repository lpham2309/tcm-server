from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from flask_serialize import FlaskSerializeMixin
from flask_mysqldb import MySQL
from flask_restful import Resource, Api, reqparse
from .settings import config
from .apis.user.user import *
from .apis.diagnosis.diagnosis import *
from .apis.symptoms.symptoms import *
from .apis.questions.questions import *
from .apis.answers.answers import *

from . import *

class TestEndpoint(Resource):
    def get(self):
        return 'Hello World'

api.add_resource(UsersAction, '/api/v1/users')
api.add_resource(SingleUserAction, '/api/v1/users/<user_id>')
api.add_resource(DoctorAction, '/api/v1/doctor/<user_id>')
api.add_resource(AssistantDoctorAction, '/api/v1/assistant_doctor/<user_id>')
api.add_resource(PatientAction, '/api/v1/patients/<user_id>')
api.add_resource(PatientDiagnosis, '/api/v1/diagnosis/<user_id>')
api.add_resource(Symptoms, '/api/v1/symptoms')
api.add_resource(Questions, '/api/v1/questions')
api.add_resource(AnswersByPatients, '/api/v1/<patient_id>')
api.add_resource(AnswersByAssistantDoctors, '/api/v1/<assistant_doctor_id>')
api.add_resource(AnswersByDoctors, '/api/v1/<doctors_id>')
api.add_resource(TestEndpoint, '/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)