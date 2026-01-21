class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def register_course(self, course):
        self.courses.append(course)


class Course:
    def __init__(self, course_code, course_title):
        self.course_code = course_code
        self.course_title = course_title


class RegistrationSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print("Registered Courses:")
            for course in student.courses:
                print(f"- {course.course_code}: {course.course_title}")
            print()


# System execution
student1 = Student("SEN001", "John Doe")
course1 = Course("SEN201", "Software Engineering")
course2 = Course("CSC202", "Data Structures")

student1.register_course(course1)
student1.register_course(course2)

system = RegistrationSystem()
system.add_student(student1)

system.display_students()
