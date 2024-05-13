from app import db
import random, string
from werkzeug.security import generate_password_hash, check_password_hash

class Person(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password_salt_hash = db.Column(db.String(128), nullable=False)
   salt = db.Column(db.String(16), nullable=False)
   win_total = db.Column(db.Integer)
   loss_total = db.Column(db.Integer)
   points_total = db.Column(db.Integer)
   guessed_words = db.relationship('GuessedWord', backref='person', lazy=True)
   themes = db.relationship('Theme', backref='person', lazy=True)

   def set_password(self, password, salt):
       self.password_salt_hash = generate_password_hash(password + salt)

   def check_password(self, password, salt):
       return check_password_hash(self.password_salt_hash, password + salt)
   
   def random_salt():
       return ''.join(random.choices(string.ascii_letters + string.digits, k=16))
       # random_salt() suggested by GitHub Copilot
   
class GuessedWord(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
   guessed_word = db.Column(db.String(12))

class Theme(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
   theme = db.Column(db.String(12), nullable=False)
   word1 = db.Column(db.String(12), nullable=False)
   word2 = db.Column(db.String(12), nullable=False)
   word3 = db.Column(db.String(12), nullable=False)
   word4 = db.Column(db.String(12), nullable=False)
   word5 = db.Column(db.String(12), nullable=False)
   word6 = db.Column(db.String(12), nullable=False)
   word7 = db.Column(db.String(12), nullable=False)
   word8 = db.Column(db.String(12), nullable=False)
   word9 = db.Column(db.String(12), nullable=False)
   word10 = db.Column(db.String(12), nullable=False)
