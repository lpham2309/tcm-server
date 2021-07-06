from tcm_project import db


class Diagnosis(db.Model):
    diagnosis_id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, unique=False, nullable=False)
    patient_id = db.Column(db.Integer, unique=False, nullable=False)
    assistant_doctor_id = db.Column(db.Integer, unique=False, nullable=False)
    doctor_notes = db.Column(db.String(255), unique=False, nullable=True)
    doctor_diagnosis = db.Column(db.String(255), unique=False, nullable=False)
    symptoms_id = db.Column(db.Integer, unique=False, nullable=False)
    syndrome_id = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, diagnosis_id, doctor_id, patient_id, assistant_doctor_id, doctor_notes, doctor_diagnosis, symptoms_id, syndrome_id):
        self.diagnosis_id = diagnosis_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.assistant_doctor_id = assistant_doctor_id
        self.doctor_notes = doctor_notes
        self.doctor_diagnosis = doctor_diagnosis
        self.symptoms_id = symptoms_id
        self.syndrome_id = syndrome_id

    def to_json2(self):
        return {
            'diagnosis_id': self.diagnosis_id,
            'doctor_id': self.doctor_id,
            'patient_id': self.patient_id,
            'assistant_doctor_id': self.assistant_doctor_id,
            'doctor_notes': self.doctor_notes,
            'doctor_diagnosis': self.doctor_diagnosis,
            'symptoms_id': self.symptoms_id,
            'syndrome_id': self.syndrome_id
        }
