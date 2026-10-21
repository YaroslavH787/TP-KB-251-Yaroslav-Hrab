def plus(x, y): return x + y
def minus(x, y): return x - y
def mnozennia(x, y): return x * y
def dilennia(x, y): 
    if y == 0: 
        return "Помилка: ділення на нуль!"
    return x / y
def calc_match(x, y, operation):
    match operation:
        case '+':
            return plus(x, y)
        case '-':
            return minus(x, y)
        case '*':
            return mnozennia(x, y)
        case '/':
            return dilennia(x, y)
        case _:
            return "Помилка: невідома операція!"
print("10 * 5 =", calc_match(10, 5, '*'))
print("10 - 2 =", calc_match(10, 2, '-'))