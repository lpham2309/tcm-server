from flask_restful import Resource, reqparse
from .. import *
from tcm_project.models.questions import Questions


def parse_questions():
    parser = reqparse.RequestParser()
    parser.add_argument('question_text', type=str, required=True)

    return parser


class QuestionController(Resource):
    """
    Add a question
    """

    def post(self):
        parse = parse_questions()
        data = parse.parse_args()

        # cursor = db.connection.cursor()
        # query = "INSERT INTO `tcm`.Questions(question_text) VALUES (%s);"
        # cursor.execute(query, (data['question_text'],))

        question = data['question_text']
        print(question)
        # current_question = Questions.query.filter_by(
        #     question_text=str(question)).first()
        # if current_question:
        #     return

        question = Questions(question_text=data['question_text'])

        db.session.add(question)
        db.session.commit()

        return {'message': 'Question added!'}, 200

    def get(self):
        try:
            results = []
            questions = Questions.query.all()

            for question in questions:
                results.append(question.to_json2())
            return results
        except Exception:
            return {
                'error': 'No questions found'
            }, 400
        return {'message': 'Successfully retrieve all questions!'}, 200
