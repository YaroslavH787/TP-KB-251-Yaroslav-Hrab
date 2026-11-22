class MathFunction:
    def plus(self, a, b): return a + b
    def minus(self, a, b): return a - b
    def mnozennia(self, a, b): return a * b
    def dilennia(self, a, b): 
        if b == 0: 
            return "Помилка: ділення на нуль!"
        return a / b