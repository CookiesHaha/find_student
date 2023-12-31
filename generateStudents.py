from student import Student, Background, Animals, Wearing
from classroom import Classroom
from studentModel import StudentModel
import random
from PIL import Image
import os

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


def generate_random_student(student_model, output_folder):
    while True:
        stu_id = f"A{random.randint(100, 999)}"

        if not student_model.check_student_existence(stu_id):
            break

    background = random.choice(list(Background))
    animals = random.choice(list(Animals))
    wearing = random.choice(list(Wearing))

    name = f"{background.value['value']}_{wearing.value['value']}_{animals.value['value']}"
    chinese_name = ""


    avatar_output_path = f"{output_folder}"

    generate_avatar(
        background.value["image_path"],
        animals.value["image_path"],
        wearing.value["image_path"],
        avatar_output_path,
        name,
    )
    avatar = f"{output_folder}/{name}.png"

    # Create a new student using the StudentModel
    new_student = Student(stu_id, name, chinese_name, background, animals, wearing, avatar)
    student_model.insert_student(new_student)
    return Student(stu_id, name, chinese_name, background, animals, wearing, avatar)

if __name__ == "__main__":
    output_folder = os.path.abspath("./img/Avatar")
    db_path = "students_data.db"
    student_model = StudentModel(db_path)
    # student_model.create_table()

    # for _ in range(24):
    #     generate_random_student(student_model, output_folder)
    
    student_model.set_chinese_name("A295","Tony Wang")

    student_model.close_connection()
    
    # 保存学生数据到文件
    # with open(students_filename, 'wb') as file:
    #     pickle.dump(classroom.students, file)

    # for student in classroom.students:
    #     print(student)
        
        
    # background_to_find = "Cloud"
    # wearing_to_find = "Flash"
    # animals_to_find = "Graff"

    # find_student(
    #     classroom.students, background_to_find, animals_to_find, wearing_to_find
    # )
