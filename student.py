import os
from enum import Enum

class Background(Enum):
    STAR = {"value": "Star", "image_path": os.path.abspath("./img/Background/01.png")}
    GALAXY = {
        "value": "Galaxy",
        "image_path": os.path.abspath("./img/Background/02.png"),
    }
    NEWWORLD = {
        "value": "NewWorld",
        "image_path": os.path.abspath("./img/Background/03.png"),
    }
    NEXTDAY = {
        "value": "NextDay",
        "image_path": os.path.abspath("./img/Background/04.png"),
    }
    CLOUD = {"value": "Cloud", "image_path": os.path.abspath("./img/Background/05.png")}
    MOUNTAIN = {
        "value": "Mountain",
        "image_path": os.path.abspath("./img/Background/06.png"),
    }


class Animals(Enum):
    BEAR = {"value": "Bear", "image_path": os.path.abspath("./img/Animals/01.png")}
    LEO = {"value": "Leo", "image_path": os.path.abspath("./img/Animals/02.png")}
    CAT = {"value": "Cat", "image_path": os.path.abspath("./img/Animals/03.png")}
    GRAFF = {"value": "Graff", "image_path": os.path.abspath("./img/Animals/04.png")}
    ROCC = {"value": "Rocc", "image_path": os.path.abspath("./img/Animals/05.png")}


class Wearing(Enum):
    FLASH = {"value": "Flash", "image_path": os.path.abspath("./img/Wearing/01.png")}
    PETS = {"value": "Pets", "image_path": os.path.abspath("./img/Wearing/02.png")}
    TREE = {"value": "Tree", "image_path": os.path.abspath("./img/Wearing/03.png")}
    VEG = {"value": "Veg", "image_path": os.path.abspath("./img/Wearing/04.png")}
    STAR = {"value": "Star", "image_path": os.path.abspath("./img/Wearing/05.png")}
    RAINBOW = {
        "value": "Rainbow",
        "image_path": os.path.abspath("./img/Wearing/06.png"),
    }

class Student:
    def __init__(self, stu_id, name, background, animals, wearing, avatar):
        self.stu_id = stu_id
        self.name = name
        self.background = background
        self.animals = animals
        self.wearing = wearing
        self.avatar = avatar
    
    def get_relative_avatar_path(self):
        # Returns the relative path of the avatar image
        return f"img/Avatar/{self.name}.png"
   
    def save_to_database(self, student_model):
        # Save the student to the database using the StudentModel
        student_model.insert_student(self)
    
    def __str__(self):
        return (
            f"Student(id={self.stu_id}, name={self.name}, "
            f"background={self.background.value}, animals={self.animals.value}, "
            f"wearing={self.wearing.value})," 
        )