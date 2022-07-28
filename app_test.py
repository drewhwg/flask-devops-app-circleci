from app import app

import unittest
import json


class CitiesTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/cities.json', content_type='application/json')
        data_test = ['Hà Nội', 'San Francisco', 'Berlin', 'New York']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), json.dumps(
            data_test))


if __name__ == '__main__':
    unittest.main()
