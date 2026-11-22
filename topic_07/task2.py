class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} років"

students = [
    Student("Олег", 20),
    Student("Анна", 18),
    Student("Дмитро", 22),
    Student("Марія", 19),
]

print("Сортування за віком:")
for student in sorted(students, key=lambda s: s.age):
    print(student)

print("\nСортування за ім'ям:")
for student in sorted(students, key=lambda s: s.name):
    print(student)