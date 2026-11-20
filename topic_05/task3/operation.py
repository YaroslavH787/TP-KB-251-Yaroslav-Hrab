def get_number():
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            return a, b
        except ValueError:
            print("Помилка: введіть коректні числа")

def oper():
    ops = ["+", "-", "*", "/"]
    while True:
        op = input("Оберіть операцію (+, -, *, /): ").strip()
        if op in ops:
            return op
        print("Помилка: невідома операція. Спробуйте ще раз")