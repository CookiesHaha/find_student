from student import Student, Background, Animals, Wearing

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, background, animals, wearing):
        # 检查输入的属性是否合法
        if background not in [bg.value['value'] for bg in Background]:
            print(f"Error: Invalid background value '{background}'.")
            return
        if animals not in [ani.value['value'] for ani in Animals]:
            print(f"Error: Invalid animals value '{animals}'.")
            return
        if wearing not in [wear.value['value'] for wear in Wearing]:
            print(f"Error: Invalid wearing value '{wearing}'.")
            return

        # 查找学生
        matching_students = [student for student in self.students if
                             student.background.value['value'] == background
                             and student.animals.value['value'] == animals
                             and student.wearing.value['value'] == wearing]

        if not matching_students:
            print(f"No student found with background '{background}', animals '{animals}', wearing '{wearing}'.")
            return

        # 返回找到的学生信息
        for student in matching_students:
            print(f"Student ID: {student.stu_id}, Name: {student.name}, Avatar: {student.avatar}")
        
        return matching_students