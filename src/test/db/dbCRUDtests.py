import unittest
from fhir.resources.patient import Patient
from flask_pymongo import PyMongo
from src.db import database
from flask import Flask
import json


class Testing(unittest.TestCase):
    # TODO use a config file for this part
    # need to start a local mongodb service for this to work - maybe move to a docker container?
    app = Flask(__name__)
    app.config['MONGO_URI'] = "mongodb://localhost:27017/testDatabase"
    mongo = PyMongo(app)

    def test_patient_CRUD(self):
        with self.app.app_context():
            patient_dict = {"resourceType": "Patient", "id": "p001", "active": True, "name": [{"text": "Adam Smith"}],
                            "birthDate": "1985-06-12"}

            patient = Patient(**patient_dict)

            database.add_patient(patient)

            patient_from_db = database.get_patient_by_id("p001")

            self.assertEqual(patient, patient_from_db)
