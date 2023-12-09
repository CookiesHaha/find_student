import os
from enum import Enum

class Background(Enum):
    STAR = {'value':'star','image_path':  os.path.abspath('./img/Background/01.png')}
    GALAXY = {'value':'galaxy','image_path': os.path.abspath('./img/Background/02.png')}
    NEWWORLD = {'value':'newWorld','image_path': os.path.abspath('./img/Background/03.png')}
    NEXTDAY = {'value':'nextDay','image_path': os.path.abspath('./img/Background/04.png')}
    CLOUD = {'value':'cloud','image_path': os.path.abspath('./img/Background/05.png')}
    MOUNTAIN = {'value':'mountain','image_path': os.path.abspath('./img/Background/06.png')}

class Animals(Enum):
    BEAR = {'value':'bear','image_path': os.path.abspath('./img/Animals/01.png')}
    LEO = {'value':'leo','image_path': os.path.abspath('./img/Animals/02.png')}
    CAT = {'value':'cat','image_path': os.path.abspath('./img/Animals/03.png')}
    GRAFF = {'value':'graff','image_path': os.path.abspath('./img/Animals/04.png')}
    ROCC = {'value':'rocc','image_path': os.path.abspath('./img/Animals/05.png')}
    
class Wearing(Enum):
    FLASH = {'value':'falsh','image_path': os.path.abspath('./img/Wearing/01.png')}
    PETS = {'value':'ptes','image_path': os.path.abspath('./img/Wearing/02.png')}
    TREE = {'value':'tree','image_path': os.path.abspath('./img/Wearing/03.png')}
    VEG = {'value':'veg','image_path': os.path.abspath('./img/Wearing/04.png')}
    STAR = {'value':'star','image_path': os.path.abspath('./img/Wearing/05.png')}
    RAINBOW = {'value':'rainbow','image_path': os.path.abspath('./img/Wearing/06.png')}

class Student:
    def __init__(self, stu_id, name, background, animals, wearing, avatar):
        self.stu_id = stu_id
        self.name = name
        self.background = background
        self.animals = animals
        self.wearing = wearing
        self.avatar = avatar

    def __str__(self):
        return (
            f"Student(id={self.stu_id}, name={self.name}, "
            f"background={self.background.value}, animals={self.animals.value}, "
            f"wearing={self.wearing.value})," 
        )