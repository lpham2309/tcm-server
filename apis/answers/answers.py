from flask_restful import Resource, reqparse
from .. import *


def parse_symptom_answers():
    parser = reqparse.RequestParser()
    parser.add_argument('question_id', type=int, required=True)
    # parser.add_argument('patient_id', type=int, required=True)
    # Switch to using user_id so we don't have to filter base on roles
    parser.add_argument('user_id', type=int, required=True)
    parser.add_argument('symptom_id', type=int, required=True)
    parser.add_argument('is_symptom', type=bool, required=True)

    return parser


class AnswersByPatients(Resource):
    def post(self):
        parse = parse_symptom_answers()
        data = parse.parse_args()

        cursor = db.connection.cursor()
        query = "INSERT INTO `tcm`.Answers(question_id, user_id, symptom_id, is_symptom) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (data['question_id'], data['user_id'],
                               data['symptom_id'], data['is_symptom'], ))

        db.connection.commit()

        return {'message': " Patient's answer has been added!"}, 200


class AnswersByAssistantDoctors(Resource):
    pass


class AnswersByDoctors(Resource):
    pass
