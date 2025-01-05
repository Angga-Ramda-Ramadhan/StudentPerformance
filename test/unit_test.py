import unittest
import json
import sys
import os
from server import app  # Import aplikasi Flask Anda
# Tambahkan path parent ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Setup aplikasi Flask untuk testing
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict_valid_input(self):
        valid_input = {
            "Socioeconomic Score": 0.9,
            "Study Hours": 7.5,
            "Sleep Hours": 8,
            "Attendance (%)": 90
        }
        response = self.app.post('/predict', data=json.dumps(valid_input), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_invalid_input(self):
        invalid_input = {
            "Socioeconomic Scre": "Invalid",
            "Study Hours": 7.5,
            "Sleep Hours": 8,
            "Attendance (%)": 90
        }
        response = self.app.post("/predict", data=json.dumps(invalid_input), content_type='application/json')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
