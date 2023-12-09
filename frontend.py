from tkinter import *
from tkinter.ttk import *

from student import Student, Background, Animals, Wearing

class Frontend:
    
    def __init__(self) -> None:
        self.root = self.__win()
        self.title = self.__create_title("Find Student", 100, 40)
        self.background_label = self.__create_label("Background", 100, 120)
        self.background_dropdown = self.__create_dropdown([bg.value['value'] for bg in Background], 200, 120)

        self.animals_label = self.__create_label("Animals", 100, 160)
        self.animals_dropdown = self.__create_dropdown([bg.value['value'] for bg in Animals], 200, 160)

        self.wearing_label = self.__create_label("Wearing", 100, 200)
        self.wearing_dropdown = self.__create_dropdown([bg.value['value'] for bg in Wearing], 200, 200)

        self.find_student = self.__create_button("Find",self.on_button_click(), 250, 250)

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

    
if __name__ == "__main__":
    frontend = Frontend()
    frontend.run()