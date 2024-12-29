from flask import current_app, g
from flask_pymongo import PyMongo
from fhir.resources.patient import Patient
import json


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = PyMongo(current_app).db

    return db


def add_patient(patient):
    """
    Inserts a patient into the patients collection.
    params:
    patient - fhir Patient resource
    """
    db = get_db()
    patient_json = patient.json()
    patient_dict = json.loads(patient_json)
    db.patients.insert_one(patient_dict)


def get_patient_by_id(id):
    """
    Retrieves a patient from the patients collection.
    params:
    id - fhir Patient id

    return:
    fhir Patient resource
    """
    db = get_db()
    try:
        patient_dict = db.patients.find_one({'id': id})
        # remove mongo id before making a patient object
        del patient_dict["_id"]
        return Patient(**patient_dict)
    # TODO specific error handling
    except Exception as e:
        return None
