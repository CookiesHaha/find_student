from enum import Enum
import random
import string
from PIL import Image
import os


class Background(Enum):
    STAR = {"value": "Star", "image_path": os.path.abspath("./img/Background/01.png")}
    GALAXY = {
        "value": "Galaxy",
        "image_path": os.path.abspath("./img/Background/02.png"),
    }
    NEWWORLD = {
        "value": "New World",
        "image_path": os.path.abspath("./img/Background/03.png"),
    }
    NEXTDAY = {
        "value": "Next Day",
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


# -------------------------------------------------------------------------------------------------------------------------------------------#


def generate_avatar(background_path, animal_path, wearing_path, output_folder, name):
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
    new_image.paste(
        background_image,
        ((new_width - bg_width) // 2, (new_height - bg_height) // 2),
        background_image,
    )
    new_image.paste(
        animal_image,
        ((new_width - ani_width) // 2, (new_height - ani_height) // 2),
        animal_image,
    )
    new_image.paste(
        wearing_image,
        ((new_width - wear_width) // 2, (new_height - wear_height) // 2),
        wearing_image,
    )

    # 合并图片
    final_image = Image.alpha_composite(
        Image.new("RGBA", new_image.size, (255, 255, 255, 255)), new_image
    )

    # 保存新图片
    os.makedirs(output_folder, exist_ok=True)
    output_path = f"{output_folder}/{name}.png"
    final_image.save(output_path)


def generate_random_student(existing_students, output_folder):
    stu_id = f"A{random.randint(100, 999)}"
    background = random.choice(list(Background))
    animals = random.choice(list(Animals))
    wearing = random.choice(list(Wearing))

    existing_students["backgrounds"].append(background)
    existing_students["animals"].append(animals)
    existing_students["wearings"].append(wearing)
    name = (
        f"{background.value['value']} {wearing.value['value']} {animals.value['value']}"
    )

    avatar_output_path = f"{output_folder}"

    generate_avatar(
        background.value["image_path"],
        animals.value["image_path"],
        wearing.value["image_path"],
        avatar_output_path,
        name,
    )
    avatar = f"{output_folder}/{name}.png"
    return Student(stu_id, name, background, animals, wearing, avatar)


def find_student(students, background, animals, wearing):
    # 检查输入的属性是否合法
    if background not in [background.value["value"] for background in Background]:
        print(f"Error: Invalid background value '{background}'.")
        return
    if animals not in [animals.value["value"] for animals in Animals]:
        print(f"Error: Invalid animals value '{animals}'.")
        return
    if wearing not in [wearing.value["value"] for wearing in Wearing]:
        print(f"Error: Invalid wearing value '{wearing}'.")
        return

    # 查找学生
    matching_students = [
        student
        for student in students
        if student.background.value["value"] == background
        and student.animals.value["value"] == animals
        and student.wearing.value["value"] == wearing
    ]

    if not matching_students:
        print(
            f"No student found with background '{background}', animals '{animals}', wearing '{wearing}'."
        )
        return

    # 返回找到的学生信息
    for student in matching_students:
        print(
            f"Student ID: {student.student_id}, Name: {student.name}, Avatar: {student.avatar}"
        )


if __name__ == "__main__":
    classroom = Classroom()
    existing_students = {"backgrounds": [], "animals": [], "wearings": []}
    output_folder = os.path.abspath("./img/Avatar")

    # for _ in range(24):
    #     random_student = generate_random_student(existing_students, output_folder)
    #     classroom.add_student(random_student)

    for student in classroom.students:
        print(student)
        
        
    # background_to_find = "Cloud"
    # wearing_to_find = "Flash"
    # animals_to_find = "Graff"

    # find_student(
    #     classroom.students, background_to_find, animals_to_find, wearing_to_find
    # )
