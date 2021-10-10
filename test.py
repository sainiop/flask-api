# try:
from src import app
from src.services import student_info
import unittest
import requests
# except Exception as e:
#     print("Some modules are missing {}".format(e))


class student_test(unittest.TestCase):
    url = "http://127.0.0.1:5000/student"

    # get all vessels
    def test_1_get_all_students(self):
        r = requests.get("{}/all".format(student_test.url))
        self.assertEqual(r.status_code, 200)

    # add  new vessel in db
    def test_2_add_new_student(self):
        test2 = {
            "name": "GitHub",
            "subject": "Testing API",
            "roll_number": "2020"
        }
        r = requests.post("{}".format(student_test.url), json=test2)
        self.assertEqual(r.status_code, 200)

    # update the vessel code and vessel name which is created in test 2
    def test_3_update_student(self):
        test3 = {
            "name": "GitHub",
            "subject": "Testing API",
            "roll_number": "2021"
        }
        r = requests.put("{}/2020".format(student_test.url), json=test3)
        self.assertEqual(r.status_code, 200)

    # delete from db above test cases
    def test_4_delete_studnet(self):
        r = requests.delete("{}/2021".format(student_test.url))
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()