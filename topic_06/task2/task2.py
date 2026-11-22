student = [
    {"name": "Andriy", "grade": 66},
    {"name": "Masha", "grade": 87},
    {"name": "Ivan", "grade": 90},
    {"name": "Dmitro", "grade": 60},
]

sorted_by_name = sorted(student, key=lambda student: student["name"])
sorted_by_grade = sorted(student, key=lambda student: student["grade"])

print("Сортування за ім'ям: ")
for s in sorted_by_name:
    print(f"{s['name']}: {s['grade']}")
print("\nСортування за оцінкою:")
for s in sorted_by_grade:
    print(f"{s['name']}: {s['grade']}")