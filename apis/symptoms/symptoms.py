from flask_restful import Resource, reqparse
from .. import *
from tcm_project.models.symptoms import Symptoms, Symptom_Subgroups
from flask import jsonify


def parse_symptoms_information():

    parser = reqparse.RequestParser()

    parser.add_argument('symptom_id', type=int)
    parser.add_argument('symptom_name', type=str, required=True)
    parser.add_argument('symptom_subgroup_id', type=int, required=True)

    return parser


def parse_symptoms_subgroup_information():

    parser = reqparse.RequestParser()

    parser.add_argument('symptom_subgroup_id', type=int)
    parser.add_argument('symptom_id', type=int)
    parser.add_argument('symptom_subgroup_name', type=str)


class SymptomsList(Resource):
    def get():
        '''
        Get a list of all symptoms
        '''
        try:
            results = []
            symptoms = Symptoms.query.limit(20).all()

            for symptom in symptoms:
                results.append(symptom.to_json2())
            return results
        except Exception:
            return {
                'error': 'No symptoms found'
            }, 400
        return {'message': 'Successfully retrieve all symptoms!'}, 200

    def post():
        '''
        Add a new symptom
        '''
        parse = parse_symptoms_information()
        data = parse.parse_args()

        new_symptom = Symptoms(
            data['symptom_id'], data['symptom_name'], data['symptom_subgroup_id'])

        db.session.add(new_symptom)
        db.session.commit()

        return {'message': 'New symptom has been added!'}, 200


class Symptoms_Subgroup(Resource):
    def get():
        '''
        Get a list of all symptoms subgroups
        '''
        try:
            results = []
            symptom_subgroups = Symptom_Subgroups.query.limit(20).all()

            for subgroup in symptom_subgroups:
                results.append(subgroup.to_json2())
            return results
        except Exception:
            return {
                'error': 'No symptoms subgroup found'
            }, 400
        return {'message': 'Successfully retrieve all subgroups!'}, 200

    def post():
        parse = parse_symptoms_subgroup_information()
        data = parse.parse_args()

        new_symptom = Symptom_Subgroups(
            data['symptom_subgroup_id'], data['symptom_id'], data['symptom_subgroup_id'])

        db.session.add(new_symptom)
        db.session.commit()

        return {'message': 'New symptom subgroup has been added!'}, 200
