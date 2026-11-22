from function import MathFunction
from operation import Logger, Operattion

class Calculator:
    def __init__(self):
        self.logger = Logger("calc.log")
        self.math = MathFunction()
        self.ops = Operattion(self.logger)

        self.action = {
            "+": self.math.plus,
            "-": self.math.minus,
            "*": self.math.mnozennia,
            "/": self.math.dilennia,
        }
    def run(self):
        self.logger.write("Запуск програми")

        a, b = self.ops.get_numbers()
        op = self.ops.get_operation()

        result = self.action[op](a, b)
        print(f"Результат: {result}")

        self.logger.write(f"Дані: a={a}, b={b} | Операція: '{op}' | Результат: {result}")
        self.logger.write("Завершення роботи\n")

if __name__ == "__main__":
    app = Calculator()
    app.run()