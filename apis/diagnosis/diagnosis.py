from flask_restful import Resource, reqparse
from .. import *
from flask import jsonify


def parse_diagnosis_information():

    parser = reqparse.RequestParser()

    parser.add_argument('diagnosis_id', type=str)
    parser.add_argument('doctor_id', type=str, required=True)
    parser.add_argument('patient_id', type=str, required=True)
    parser.add_argument('assistant_doctor_id', type=str, required=True)
    parser.add_argument('doctor_notes', type=str)
    parser.add_argument('doctor_diagnosis', type=str)
    parser.add_argument('symptoms_id', type=str,
                        action='append', required=True)
    parser.add_argument('syndrome_id', type=str, required=True)

    return parser


def parse_update_diagnosis_information():

    parser = reqparse.RequestParser()

    parser.add_argument('doctor_id', type=str)
    parser.add_argument('assistant_doctor_id', type=str)
    parser.add_argument('doctor_notes', type=str)
    parser.add_argument('doctor_diagnosis', type=str)
    parser.add_argument('symptoms_id', type=str, action='append')
    parser.add_argument('syndrome_id', type=str)

    return parser


class PatientDiagnosis(Resource):
    def get(self, patient_id):
        cursor = db.connection.cursor()
        query = "SELECT * FROM `tcm`.diagnosis INNER JOIN `tcm`.users ON " \
            "diagnosis.patient_id = users.user_id WHERE patient_id=%s;"
        cursor.execute(query, (str(patient_id),))

        try:
            result = cursor.fetchone()
        except Exception:
            return {
                'error': 'No diagnosis information found with current user'
            }, 400

        return jsonify(result)

    def put(self, patient_id):
        parse = parse_update_diagnosis_information()
        data = parse.parse_args()

        cursor = db.connection.cursor()

        query = "UPDATE `tcm`.diagnosis SET doctor_id=%s, assistant_doctor_id=%s, doctor_notes=%s, doctor_diagnosis=%s, symptoms_id=%s, syndrome_id=%s WHERE patient_id=%s;"
        cursor.execute(query, (data['doctor_id'], data['assistant_doctor_id'], data['doctor_notes'],
                               data['doctor_diagnosis'], data['symptoms_id'], data['syndrome_id'], patient_id,))

        db.connection.commit()

        return {'message': 'Successfully update information of a patient'}, 200


class DiagnosisInformation(Resource):
    def post(self):
        parse = parse_diagnosis_information()
        data = parse.parse_args()

        cursor = db.connection.cursor()
        query = "INSERT INTO `tcm`.diagnosis(diagnosis_id, doctor_id, patient_id, assistant_doctor_id, doctor_notes, doctor_diagnosis, symptoms_id, syndrome_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (data['diagnosis_id'], data['doctor_id'], data['patient_id'], data['assistant_doctor_id'],
                               data['doctor_notes'], data['doctor_diagnosis'], data['symptoms_id'], data['syndrome_id'],))
        db.connection.commit()

        return {'message': 'New diagnosis created!'}, 200
