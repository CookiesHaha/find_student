from tkinter import *
from tkinter.ttk import *
import pickle
from student import Student, Background, Animals, Wearing
from classroom import Classroom
class Frontend:
    
    def __init__(self) -> None:
        self.root = self.__win()
        self.classroom = Classroom()
        self.students_filename = "students_data.pkl"
    
        with open(self.students_filename, 'rb') as file:
            self.classroom.students = pickle.load(file)

        self.title = self.__create_title("Find Student", 100, 40)
        self.background_label = self.__create_label("Background", 100, 120)
        self.background_dropdown = self.__create_dropdown([bg.value['value'] for bg in Background], 200, 120)

        self.animals_label = self.__create_label("Animals", 100, 160)
        self.animals_dropdown = self.__create_dropdown([bg.value['value'] for bg in Animals], 200, 160)

        self.wearing_label = self.__create_label("Wearing", 100, 200)
        self.wearing_dropdown = self.__create_dropdown([bg.value['value'] for bg in Wearing], 200, 200)

        self.find_student = self.__create_button("Find",self.find_student_command, 250, 240)

    def __win(self):
        root = Tk()
        root.title("Find Student")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(geometry)
        root.resizable(width=False, height=False)
        return root
    
    def run(self):
        self.root.mainloop()
    
    def __create_title(self, text, x, y):
        label = Label(self.root, text=text, font=('Jura', 24))
        
        label.place(x=x, y=y, width=400, height=48)
        return label
    
    def __create_label(self, text, x, y):
        label = Label(self.root, text=text)
        label.place(x=x, y=y, width=80, height=24)
        return label
    
    def __create_dropdown(self, values, x, y):
        var = StringVar()
        var.set(values[0])  # Set the default value
        dropdown = Combobox(self.root, textvariable=var, values=values)
        dropdown.place(x=x, y=y, width=240, height=24)
        return dropdown
    
    def __create_button(self, text, command, x, y):
        button = Button(self.root, text=text, command=command)
        button.place(x=x, y=y, width=120, height=30)
        return button
    
    def __config_lable(self, text, x, y):
        config_lable = Label(self.root, text=text)
        config_lable.place(x=x, y=y, width=1000, height=24)
    
    def find_student_command(self):
        # 获取下拉框的当前值
        background_value = self.background_dropdown.get()
        animals_value = self.animals_dropdown.get()
        wearing_value = self.wearing_dropdown.get()

        # 调用Classroom中的find_student方法
        matching_student = self.classroom.find_student(background_value, animals_value, wearing_value)
        # for student in matching_student:
        #     print(f"Student ID: {student.stu_id}, Name: {student.name}, Avatar: {student.avatar}")

        if matching_student:
            # 显示第一个匹配学生的信息（你可以根据需要选择其他方式显示多个匹配学生的信息）
            student = matching_student
            student_info = (f"Student ID: {student.stu_id}, Name: {student.name}")
            print(student_info)
            # 显示信息
            self.__config_lable(text=student_info, x=100, y=280)
        else:
            no_student_info = ("No matching student found.")
            print(no_student_info)
            self.__config_lable(text=no_student_info, x=100, y=280)
        print(background_value, animals_value, wearing_value)
    
if __name__ == "__main__":
    output_folder = "img/Avatar"
    # students_filename = "students_data.pkl"
    
    # with open(students_filename, 'rb') as file:
    #     classroom.students = pickle.load(file)
    
    # for student in classroom.students:
    #     print(student.name)
    
    # # background_to_find = "galaxy"
    # # animals_to_find = "cat"
    # # wearing_to_find = "rainbow"

    # # classroom.find_student(background_to_find, animals_to_find, wearing_to_find)

    frontend = Frontend()
    frontend.run()

