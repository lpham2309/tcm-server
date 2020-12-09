from tcm_project import db


class Questions(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, question_text):
        self.question_text = question_text

    def to_json2(self):
        return {
            'question_id': self.question_id,
            'question_text': self.question_text,
        }
