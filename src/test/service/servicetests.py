import flask_unittest

from src.service import service


class Testing(flask_unittest.ClientTestCase):
    service_url = "http://127.0.0.1:5000"
    app = service.create_app()

    def test_load_patients(self, client):
        with self.app.app_context():
            response = client.get('/patients/load')
            print(response)
            
