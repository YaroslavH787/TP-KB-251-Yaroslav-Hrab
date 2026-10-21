import math
def discriminant(a, b, c):
    return b**2 - 4 * a * c
def roots(a, b, c):
    if a == 0:
        return "Помилка, 'a' не може дорівнювати 0"
    d = discriminant(a, b, c)
    print(f"D = {d}") # виводить текст "D = " та підставляє значення змінної d
    if d > 0:
        x1 = (-b + math.sqrt(d) / (2*a))
        x2 = (-b - math.sqrt(d) / (2*a))
        return f"Рівняння має два дійсних корені: x1 = {x1}, x2 = {x2}"
    elif d == 0:
        x = -b / (2*a)
        return f"Рівняння має один дійсний корінь: x = {x}"
    else:
        return "Рівняння не має дійсних коренів (D < 0)."

a, b, c = 1, -5, 6
print(roots(a, b, c))