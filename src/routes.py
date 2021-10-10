from src.models import StudentsSchema
from src import app
from src.services import student_info


studentInfo = student_info()

student_schema = StudentsSchema
students_schema = StudentsSchema(many=True)

# test server
@app.route("/", methods=["GET"])
def hello():
    return studentInfo.hello_test()


# add new student
@app.route("/student", methods=["POST"])
def new_student():
    return studentInfo.add_student()


# Get All students info
@app.route("/student/all", methods=["GET"])
def all_students():
    return studentInfo.get_students()

#get a student by roll number
@app.route("/student/<roll_number>", methods=["GET"])
def student(roll_number):
    return studentInfo.get_student(roll_number)


# Update a student info roll_number
@app.route("/student/<roll_number>", methods=["PUT"])
def update_student(roll_number):
    return studentInfo.update_student(roll_number)


# Delete Product
@app.route('/student/<roll_number>', methods=['DELETE'])
def remove_student(roll_number):
    return studentInfo.delete_student(roll_number)
