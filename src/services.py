#!/usr/bin/python
import json
from flask import request, jsonify
from src.models import myStudents, StudentsSchema

# import db instance
from src import db

student_schema = StudentsSchema
students_schema = StudentsSchema(many=True)


# services or model for vessel api
class student_info:
    # test api
    def hello_test(self):
        return "Hello Students!"

    # add student
    def add_student(self):
        name = request.json["name"]
        subject = request.json["subject"]
        roll_number = request.json["roll_number"]

        newStudent = myStudents(name, subject, roll_number)

        db.session.add(newStudent)
        db.session.commit()

        return student_schema.jsonify(newStudent)

    # get all students
    def get_students(self):
        all_student = myStudents.query.all()
        result1 = students_schema.dump(all_student)
        return jsonify(result1)

    # get student by roll number
    def get_student(self, roll_number):
        student1 = myStudents.query.get(roll_number)
        return student_schema.jsonify(student1)

    # update student information by id
    def update_student(self, roll_number):
        student3 = myStudents.query.get(roll_number)

        name = request.json["name"]
        subject = request.json["subject"]
        roll_number = request.json["roll_number"]

        student3.name = name
        student3.subject = subject
        student3.roll_number = roll_number

        db.session.commit()

        return student_schema.jsonify(student3)

    # Delete student info
    def delete_student(self, roll_number):
        student = myStudents.query.get(roll_number)
        db.session.delete(student)
        db.session.commit()

        return student_schema.jsonify('student')
