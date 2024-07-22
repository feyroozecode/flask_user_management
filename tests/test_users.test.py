from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import unittest

# init db
db = SQLAlchemy()

# User model for database table users with columns id, username, password 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

# Test User model
class UserTest(unittest.TestCase):
    def test_set_password(self):
        user = User()
        password = "password123"
        user.set_password(password)
        self.assertTrue(check_password_hash(user.password, password))

    def test_check_password(self):
        user = User()
        password = "password123"
        user.set_password(password)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.check_password("wrongpassword"))

if __name__ == '__main__':
    unittest.main()