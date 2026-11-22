from datetime import datetime

class Logger:
    def __init__(self, filename="calc.log"):
        self.filename = filename

    def write(self, message):
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"[{time_now}] {message}\n")

class Operattion:
    def __init__(self, logger):
        self.logger = logger
        self.valid_ops = ["+", "-", "*", "/"]

    def get_numbers(self):
        while True:
            try:
                a = float(input("Введіть перше число: "))
                b = float(input("Введіть друге число: "))
                return a, b
            except ValueError:
                self.logger.write("Помилка вводу: користувач ввів не число")
                print("Помилка: введіть коректні числа")

    def get_operation(self):
        while True:
            op = input("Оберіть операцію (+, -, *, /): ").strip()
            if op in self.valid_ops:
                return op
            self.logger.write(f"Помилка вводу: невідома операція '{op}'")
            print("Помилка: невідома операція. Спробуйте ще раз")