from tkinter import *
from tkinter.ttk import *
import sqlite3  # 导入sqlite3库
from student import Student, Background, Animals, Wearing
from studentModel import StudentModel
from random import shuffle

class Frontend:
    
    def __init__(self) -> None:
        self.root = self.__win()
        self.student_model = StudentModel("students_data.db")

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
        height = 600
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
    
    def __config_label(self, text, x, y):
        config_lable = Label(self.root, text=text)
        config_lable.place(x=x, y=y, width=1000, height=24)

    def __image_display(self, image_path, x, y, width, height):
        image = PhotoImage(file=image_path)
        image_lable = Label(self.root, image=image)
        image_lable.image=image
        image_lable.place(x=x, y=y, width=width, height=height)
    
    def __image_clean(self, x, y, width, height):
        blank_image = PhotoImage(width=1, height=1)  # Create a blank image
        blank_label = Label(self.root, image=blank_image)
        blank_label.image = blank_image
        blank_label.place(x=x, y=y, width=width, height=height)
        self.root.update()  # Force update to clear the image

    def __shuffle_image(self, x, y, width, height):
        avatars = self.student_model.get_all_avatars()
        # 设置洗牌的速度参数
        initial_speed = 50  # 初始速度
        acceleration = 10  # 加速度
        
        shuffle(avatars)

        for avatar_path in avatars:
            self.__image_display(avatar_path, x=x, y=y, width=width, height=height)
            self.root.update()
            self.root.after(initial_speed) 
            initial_speed += acceleration
        self.__image_clean(x=x, y=y, width=width, height=height)

    def find_student_command(self):
        background_value = self.background_dropdown.get()
        print(background_value)
        animals_value = self.animals_dropdown.get()
        print(animals_value)
        wearing_value = self.wearing_dropdown.get()
        print(wearing_value)
        
        
        self.__shuffle_image(x=180, y=300, width=280, height=280)
        
        matching_student = self.student_model.find_student(background_value, animals_value, wearing_value)

        if matching_student:
            student_info = f"Student ID: {matching_student.stu_id}, Name: {matching_student.name}"
            print(student_info)
            self.__config_label(text=student_info, x=100, y=280)
            self.__image_display(matching_student.avatar, x=180, y=300, width=280, height=280)
        else:
            no_student_info = "No matching student found."
            print(no_student_info)
            self.__config_label(text=no_student_info, x=100, y=280)
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

