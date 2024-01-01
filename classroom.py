import sqlite3
from student import Student, Background, Animals, Wearing


class Classroom:
    def __init__(self, student_model):
        self.student_model = student_model
        self.create_table()

    def create_table(self):
        # Let the StudentModel handle table creation
        self.student_model.create_table()

    def add_student(self, student):
        # Use the StudentModel to insert a student
        self.student_model.insert_student(student)

    # def find_student(self, background, animals, wearing):
    #     # Validate input
    #     if background not in [bg.value['value'] for bg in Background]:
    #         print(f"Error: Invalid background value '{background}'.")
    #         return None
    #     if animals not in [ani.value['value'] for ani in Animals]:
    #         print(f"Error: Invalid animals value '{animals}'.")
    #         return None
    #     if wearing not in [wear.value['value'] for wear in Wearing]:
    #         print(f"Error: Invalid wearing value '{wearing}'.")
    #         return None

    #     # Use the StudentModel to fetch students
    #     students = self.student_model.fetch_students_by_attributes(background, animals, wearing)

    #     if students:
    #         # Display the first matching student
    #         student = students[0]
    #         print(f"Student ID: {student.stu_id}, Name: {student.name}, Avatar: {student.avatar}")
    #         return student

    #     print(f"No student found with background '{background}', animals '{animals}', wearing '{wearing}'.")
    #     return None