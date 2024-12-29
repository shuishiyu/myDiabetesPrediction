import os

from flask import Flask, render_template
import requests
from flask_pymongo import PyMongo

PUBLIC_FHIR_URL_PATIENT = 'http://hapi.fhir.org/baseR4/Patient'


def create_app():
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    # TODO change these variables depending on frontend directory structure
    STATIC_FOLDER = os.path.join(APP_DIR, '../webapp/static')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, '../webapp')

    app = Flask(__name__, static_folder=STATIC_FOLDER,
                template_folder=TEMPLATE_FOLDER,
                )

    # TODO use a config file for this part
    # need to start a local mongodb service for this to work - maybe move to a docker container?
    app.config['MONGO_URI'] = "mongodb://localhost:27017/testDatabase"
    mongo = PyMongo(app)

    @app.route('/health')
    def health():
        return 'The server is up and running'

    @app.route('/patients')
    def get_patients():
        results = requests.get(PUBLIC_FHIR_URL_PATIENT)
        results.json()
        return results.json()['entry']

    @app.route('/patients/load')
    def load_patients():
        # TODO implement this if we need it
        """
        Add patients from the FHIR server to the DB

        :return:
        the list of patients from the fhir server
        """
        results = requests.get(PUBLIC_FHIR_URL_PATIENT)
        results.json()
        return results.json()['entry']

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        return render_template('index.html')

    return app
