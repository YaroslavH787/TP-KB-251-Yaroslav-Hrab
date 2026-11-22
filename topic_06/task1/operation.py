from datetime import datetime

def write_log(message):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calc.log", "a", encoding="utf-8") as file:
        file.write(f"[{time_now}] {message}\n")

def get_numbers():
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            return a, b
        except ValueError:
            write_log("Помилка вводу: користувач ввів не число")
            print("Помилка: введіть коректні числа")

def oper():
    ops = ["+", "-", "*", "/"]
    while True:
        op = input("Оберіть операцію (+, -, *, /): ").strip()
        if op in ops:
            return op
        write_log(f"Помилка вводу: невідома операція '{op}'")
        print("Помилка: невідома операція. Спробуйте ще раз.")