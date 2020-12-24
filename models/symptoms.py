from tcm_project import db


class Symptoms(db.Model):
    symptom_id = db.Column(db.Integer, primary_key=True)
    symptom_name = db.Column(db.String(255), unique=False, nullable=False)
    symptom_subgroup_id = db.Column(
        db.String(255), unique=False, nullable=False)

    def __init__(self, symptom_id, symptom_name, symptom_subgroup_id):
        self.symptom_id = symptom_id
        self.symptom_name = symptom_name
        self.symptom_subgroup_id = symptom_subgroup_id

    def to_json2(self):
        return {
            'symptom_id': self.symptom_id,
            'symptom_name': self.symptom_name,
            'symptom_subgroup_id': self.symptom_subgroup_id,
        }


class Symptom_Subgroups(db.Model):
    symptom_subgroup_id = db.Column(db.Integer, primary_key=True)
    symptom_id = db.Column(db.String(255), unique=False, nullable=False)
    symptom_subgroup_name = db.Column(
        db.String(255), unique=False, nullable=False)

    def __init__(self, symptom_subgroup_id, symptom_id, symptom_subgroup_name):
        self.symptom_subgroup_id = symptom_subgroup_id
        self.symptom_id = symptom_id
        self.symptom_subgroup_name = symptom_subgroup_name

    def to_json2(self):
        return {
            'symptom_subgroup_id': self.symptom_subgroup_id,
            'symptom_id': self.symptom_id,
            'symptom_subgroup_name': self.symptom_subgroup_name
        }
