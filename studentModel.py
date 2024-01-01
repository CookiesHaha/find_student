import sqlite3
from student import Student, Background, Animals, Wearing

class StudentModel:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)

    def create_table(self):
        # Create the 'students' table if it doesn't exist
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    stu_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    chinese_name TEXT DEFAULT '',
                    background TEXT NOT NULL,
                    animals TEXT NOT NULL,
                    wearing TEXT NOT NULL,
                    avatar TEXT NOT NULL
                )
            ''')

    def insert_student(self, student):
        # Insert a student into the 'students' table
        with self.connection:
            self.connection.execute('''
                INSERT INTO students (stu_id, name, background, animals, wearing, avatar)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (student.stu_id, student.name, student.background.value['value'],
                  student.animals.value['value'], student.wearing.value['value'], student.avatar))

    def fetch_all_students(self):
        # Fetch all students from the 'students' table
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM students')

        students = []
        for row in cursor.fetchall():
            stu_id, name, chinese_name, background, animals, wearing, avatar = row
            background_enum = next((m for m in Background if m.value['value'].lower() == background.lower()), None)
            animals_enum = next((m for m in Animals if m.value['value'].lower() == animals.lower()), None)
            wearing_enum = next((m for m in Wearing if m.value['value'].lower() == wearing.lower()), None)

            if background_enum and animals_enum and wearing_enum:
                student = Student(stu_id, name, chinese_name, background_enum, animals_enum, wearing_enum, avatar)
                students.append(student)

        cursor.close()
        return students
    
    def check_student_existence(self, stu_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT COUNT(*) FROM students WHERE stu_id = ?', (stu_id,))
            count = cursor.fetchone()[0]
            return count > 0
    
    def get_all_avatars(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('SELECT avatar FROM students')
            return [row[0] for row in cursor.fetchall()]
        
    def find_student(self, background, animals, wearing):
        # Check if the input values are valid
        valid_backgrounds = [bg.value['value'] for bg in Background]
        # print(valid_backgrounds)
        valid_animals = [ani.value['value'] for ani in Animals]
        # print(valid_animals)
        valid_wearing = [wear.value['value'] for wear in Wearing]
        # print(valid_wearing)

        if background not in valid_backgrounds:
            print(f"Error: Invalid background value '{background}'.")
            return None
        if animals not in valid_animals:
            print(f"Error: Invalid animals value '{animals}'.")
            return None
        if wearing not in valid_wearing:
            print(f"Error: Invalid wearing value '{wearing}'.")
            return None

        # print(f"Background: {background}, Animals: {animals}, Wearing: {wearing}")
        cursor = self.connection.cursor()
        # for row in cursor.fetchall():
        #     stu_id, name, background, animals, wearing, avatar = row
        #     print(f"Database row - Background: '{background}', Animals: '{animals}', Wearing: '{wearing}'")

        cursor.execute('''
            SELECT stu_id, name, chinese_name, avatar
            FROM students
            WHERE background = ? AND animals = ? AND wearing = ?
        ''', (background, animals, wearing))

        result = cursor.fetchone()
        if result:
            stu_id, name, chinese_name, avatar = result
            print(f"Student ID: {stu_id}, Name: {name}, Chinese Name: {chinese_name} Avatar: {avatar}")
            return Student(stu_id, name, chinese_name, background, animals, wearing, avatar)

        print(f"No student found with background '{background}', animals '{animals}', wearing '{wearing}'.")
        return None
    
    def set_chinese_name(self, stu_id, chinese_name):
        with self.connection:
            self.connection.execute('''
                UPDATE students
                SET chinese_name = ?
                WHERE stu_id = ?
            ''', (chinese_name, stu_id))
  
    def close_connection(self):
        self.connection.close()