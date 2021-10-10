from src import db, app
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)


class myStudents(db.Model):
    name = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    roll_number = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)

    def __init__(self, name, subject, roll_number):
        self.name = name
        self.subject = subject
        self.roll_number = roll_number


#Students Schema/model
class StudentsSchema(ma.Schema):
    class Meta:
        fields = ("name", "subject", "roll_number")

db.create_all()
