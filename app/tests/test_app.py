import unittest
from app import app, db
from app.models import User

class UserManagerTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        response = self.client.post('/register', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password1'
        })
        self.assertEqual(response.status_code, 201)

    def test_register_duplicate_email(self):
        self.client.post('/register', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password1'
        })
        response = self.client.post('/register', json={
            'name': 'Jane Doe',
            'email': 'john@example.com',
            'password': 'password2'
        })
        self.assertEqual(response.status_code, 400)

    def test_login_success(self):
        self.client.post('/register', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password1'
        })
        response = self.client.post('/login', json={
            'email': 'john@example.com',
            'password': 'password1'
        })
        self.assertEqual(response.status_code, 200)

    def test_login_failure(self):
        response = self.client.post('/login', json={
            'email': 'nonexistent@example.com',
            'password': 'password1'
        })
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
