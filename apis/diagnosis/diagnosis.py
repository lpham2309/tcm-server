from flask_restful import Resource, reqparse
from .. import *

def parse_diagnosis_information():

    parser = reqparse.RequestParser()

    parser.add_argument('diagnosis_id', type=str, required=True)
    parser.add_argument('doctor_id', type=str, required=True)
    parser.add_argument('assistant_doctor_id', type=str, required=True)
    parser.add_argument('patient_id', type=str, required=True)
    parser.add_argument('doctor_notes', type=str)
    parser.add_argument('symptoms_id', type=str, action='append', required=True)
    parser.add_argument('syndrome_id', type=str, required=True)

    return parser

class PatientDiagnosis(Resource):
    def get(self, patient_id):
        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.diagnosis WHERE patient_id=%s;"
        cursor.execute(query, (str(patient_id),))

        result = cursor.fetchone()

        return {'message': 'Successfully get diagnosis information of a patient'}, 200
    
    def put(self, patient_id):
        parse = parse_diagnosis_information()
        data = parse.parse_args()

        cursor = db.connection.cursor()

        query = "UPDATE `tcm`.diagnosis SET doctor_notes=%s WHERE diagnosis_id=%s;"
        cursor.execute(query, (data['doctor_notes'], data['diagnosis_id'],))

        db.connection.commit()

        return {'message': 'Successfully update information of a patient'}, 200
    
    def post(self, patient_id):
        parse = parse_diagnosis_information()
        data = parse.parse_args()

        cursor = db.connection.cursor()
        query = "INSERT INTO `tcm`.diagnosis(diagnosis_id, assistant_doctor_id, patient_id, assistant_doctor_notes, doctor_notes, symptoms_id, syndrome_id) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (data['diagnosis_id'], data['assistant_doctor_id'], data['patient_id'], data['assistant_doctor_notes'], data['doctor_notes'], data['symptoms_id'], data['syndrome_id'],))
        db.connection.commit()

        return {'message': 'New diagnosis created!'}, 200