def plus(x, y): return x + y
def minus(x, y): return x - y
def mnozennia(x, y): return x * y
def dilennia(x, y): 
    if y == 0: 
        return "Помилка: ділення на нуль!"
    return x / y
def calc(x, y, operation):
    if operation == '+':
        return plus(x, y)
    elif operation == '-':
            return minus(x, y)
    elif operation == '*':
            return mnozennia(x, y)
    elif operation == '/':
            return dilennia(x, y)
    else: 
          return "Помилка: невідома операція!"
print("10 + 5 = ", calc(10, 5, '+'))
print("10 / 0 = ", calc(10, 0, '/'))
    