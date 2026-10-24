class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        teacher.add_student(self)

    def show_teacher(self):
        print(f"{self.name}'s teacher is {self.teacher.name}.")


# Create the objects
teacher = Teacher("Ms. Cruz")
student1 = Student("Alex", teacher)
student2 = Student("Jordan", teacher)

# Show the association
student1.show_teacher()
student2.show_teacher()

print("Students of", teacher.name + ":")
for student in teacher.students:
    print(student.name)
