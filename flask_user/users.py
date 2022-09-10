import base64
import datetime
from flask_user import UserMixin
from mongoengine import Document,StringField,IntField,BinaryField,DateTimeField
from werkzeug.security import check_password_hash


class User(Document,UserMixin):
    username = StringField(unique=True, required=True)
    password = StringField(required=True)
    age = IntField()
    

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)

class ConfigClass(object):
    # Flask-MongoEngine settings
    MONGODB_SETTINGS = {
        'db': 'mydb',
        'host': 'mongodb://localhost:27017/mydb'
    }