from flask_restful import Resource, reqparse
from .. import *


def parse_questions():
    parser = reqparse.RequestParser()
    parser.add_argument('question_text', type=str, required=True)

    return parser


class Questions(Resource):
    """
    Add a question
    """

    def post(self):
        parse = parse_questions()
        data = parse.parse_args()

        cursor = db.connection.cursor()
        query = "INSERT INTO `tcm`.Questions(question_text) VALUES (%s);"
        cursor.execute(query, (data['question_text'],))

        db.connection.commit()

        return {'message': 'Question added!'}, 200
