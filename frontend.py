from tkinter import *
from tkinter.ttk import *
from student import Background, Animals, Wearing
from studentModel import StudentModel
from random import shuffle

class CommonFrame(Frame):
    def __init__(self, parent, student_model):
        super().__init__(parent)
        self.student_model = student_model

    def create_title(self, text, x, y):
        label = Label(self, text=text, font=('Jura', 24))
        label.place(x=x, y=y, width=400, height=48)
        return label

    def create_label(self, text, x, y):
        label = Label(self, text=text)
        label.place(x=x, y=y, width=80, height=24)
        return label

    def create_dropdown(self, values, x, y):
        var = StringVar()
        var.set(values[0])  # Set the default value
        dropdown = Combobox(self, textvariable=var, values=values)
        dropdown.place(x=x, y=y, width=240, height=24)
        return dropdown

    def create_button(self, text, command, x, y):
        button = Button(self, text=text, command=command)
        button.place(x=x, y=y, width=120, height=30)
        return button

    def config_label(self, text, x, y):
        config_label = Label(self, text=text)
        config_label.place(x=x, y=y, width=1000, height=24)

    def image_display(self, image_path, x, y, width, height):
        image = PhotoImage(file=image_path)
        image_label = Label(self, image=image)
        image_label.image = image
        image_label.place(x=x, y=y, width=width, height=height)

    def image_clean(self, x, y, width, height):
        blank_image = PhotoImage(width=1, height=1)  # Create a blank image
        blank_label = Label(self, image=blank_image)
        blank_label.image = blank_image
        blank_label.place(x=x, y=y, width=width, height=height)
        self.update()  # Force update to clear the image

class FindStudentFrame(CommonFrame):
    def __init__(self, parent, student_model):
        super().__init__(parent, student_model)
        self.create_widgets()

    def create_widgets(self):
        self.title = self.create_title("Find Student", 100, 40)
        self.background_label = self.create_label("Background", 100, 120)
        self.background_dropdown = self.create_dropdown([bg.value['value'] for bg in Background], 200, 120)

        self.animals_label = self.create_label("Animals", 100, 160)
        self.animals_dropdown = self.create_dropdown([bg.value['value'] for bg in Animals], 200, 160)

        self.wearing_label = self.create_label("Wearing", 100, 200)
        self.wearing_dropdown = self.create_dropdown([bg.value['value'] for bg in Wearing], 200, 200)

        self.find_student = self.create_button("Find", self.find_student_command, 250, 240)

    def __shuffle_image(self, x, y, width, height):
        avatars = self.student_model.get_all_avatars()
        # 设置洗牌的速度参数
        initial_speed = 50  # 初始速度
        acceleration = 10  # 加速度

        shuffle(avatars)

        for avatar_path in avatars:
            self.image_display(avatar_path, x=x, y=y, width=width, height=height)
            self.update()
            self.after(initial_speed)
            initial_speed += acceleration
        self.image_clean(x=x, y=y, width=width, height=height)

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
            self.config_label(text=student_info, x=100, y=280)
            self.image_display(matching_student.avatar, x=180, y=300, width=280, height=280)
        else:
            no_student_info = "No matching student found."
            print(no_student_info)
            self.config_label(text=no_student_info, x=100, y=280)


class SetNameFrame(CommonFrame):
    def __init__(self, parent, student_model):
        super().__init__(parent, student_model)        
        self.current_student_index = 0  # Index to track the current student
        self.students = self.student_model.fetch_all_students()  # Fetch all students
        self.create_widgets()

    def create_widgets(self):
        self.title = self.create_title("Set Name", 100, 40)
        # Display initial student information
        self.display_student_info()

        # Button to switch to the next student
        next_student_button = self.create_button("Next Student", self.next_student_command, 250, 240)
        previous_student_button = self.create_button("Previous Student", self.previous_student_command, 100, 240)

    def display_student_info(self):
        # Display student information based on the current index
        if 0 <= self.current_student_index < len(self.students):
            current_student = self.students[self.current_student_index]
            student_info = f"Student ID: {current_student.stu_id}, Name: {current_student.name}"
            self.config_label(text=student_info, x=100, y=280)
            self.image_display(current_student.avatar, x=180, y=300, width=280, height=280)
        else:
            # No more students to display
            self.config_label(text="No more students.", x=100, y=280)
            self.image_clean(x=180, y=300, width=280, height=280)

    def next_student_command(self):
        # Move to the next student
        self.current_student_index += 1
        # Display information for the next student
        self.display_student_info()
    
    def previous_student_command(self):
        # Move to the previous student
        self.current_student_index -= 1
        # Display information for the previous student
        self.display_student_info()
        if self.current_student_index < 0:
            # Reset to the last student if at the beginning
            self.current_student_index = len(self.students) - 1
            self.display_student_info()


class Frontend:
    def __init__(self):
        self.root = self.__win()
        self.notebook = Notebook(self.root)
        self.student_model = StudentModel("students_data.db")

        # Create Find Student Frame
        self.find_student_frame = FindStudentFrame(self.notebook, student_model=StudentModel("students_data.db"))
        self.notebook.add(self.find_student_frame, text="Find Student")

        # Create Set Name Frame
        self.set_name_frame = SetNameFrame(self.notebook, student_model=StudentModel("students_data.db"))
        self.notebook.add(self.set_name_frame, text="Set Name")

        self.notebook.pack(expand=True, fill="both")

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


if __name__ == "__main__":
    frontend = Frontend()
    frontend.run()
