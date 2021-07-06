from tcm_project import db


class AnswerController(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), unique=False, nullable=False)
    symptom_id = db.Column(db.Integer, unique=False, nullable=False)
    is_symptom = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, question_id, user_id, symptom_id, is_symptom):
        self.question_id = question_id
        self.user_id = user_id
        self.symptom_id = symptom_id
        self.is_symptom = is_symptom

    def to_json2(self):
        return {
            'question_id': self.question_id,
            'user_id': self.user_id,
            'symptom_id': self.symptom_id,
            'is_symptom': self.is_symptom
        }
