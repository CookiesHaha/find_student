from enum import Enum
import random
import string
from PIL import Image
import os

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
       
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student_by_attributes(self, background, animals, wearing):
        for student in self.students:
            if (
                student.background == background
                and student.animals == animals
                and student.wearing == wearing 
            ):
                return student
            return None

def generate_avatar(background_path, animal_path, wearing_path, output_path):
    # 打开三张图片
    background_image = Image.open(background_path).convert("RGBA")
    animal_image = Image.open(animal_path).convert("RGBA")
    wearing_image = Image.open(wearing_path).convert("RGBA")

    # 获取每张图片的宽度和高度
    bg_width, bg_height = background_image.size
    ani_width, ani_height = animal_image.size
    wear_width, wear_height = wearing_image.size

    # 计算新图片的宽度和高度
    new_width = max(bg_width, ani_width, wear_width)
    new_height = max(bg_height, ani_height, wear_height)

    # 创建一个新的图片，初始化为透明背景
    new_image = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))

    # 将三张图片堆叠到新图片上
    new_image.paste(background_image, ((new_width - bg_width) // 2, (new_height - bg_height) // 2), background_image)
    new_image.paste(animal_image, ((new_width - ani_width) // 2, (new_height - ani_height) // 2), animal_image)
    new_image.paste(wearing_image, ((new_width - wear_width) // 2, (new_height - wear_height) // 2), wearing_image)

    # 合并图片
    final_image = Image.alpha_composite(Image.new("RGBA", new_image.size, (255, 255, 255, 255)), new_image)

    # 保存新图片
    final_image.save(output_path)
        
def generate_random_student(existing_students):
    stu_id = f"A{random.randint(100, 999)}"
    background = random.choice(list(Background))
    animals = random.choice(list(Animals))
    wearing = random.choice(list(Wearing))

    existing_students["backgrounds"].append(background)
    existing_students["animals"].append(animals)
    existing_students["wearings"].append(wearing)
    
    avatar_output_path = f"avatar_{stu_id}.png"
    generate_avatar(background.value["image_path"], animals.value["image_path"], wearing.value["image_path"], avatar_output_path)
    avatar = avatar_output_path
   
    name = f"{background} {animals} {wearing}"

    return Student(stu_id, name, background, animals, wearing, avatar)

if __name__ == "__main__":
    classroom = Classroom()
    existing_students = {"backgrounds": [], "animals": [], "wearings": []}

    for _ in range(24):
        random_student = generate_random_student(existing_students)
        classroom.add_student(random_student)
    
    for student in classroom.students:
        print(student)