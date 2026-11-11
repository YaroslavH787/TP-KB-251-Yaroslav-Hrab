def plus(x, y): return x + y
def minus(x, y): return x - y
def mnozennia(x, y): return x * y
def dilennia(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"

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

def chisla(promt_text):
    while True:
        vvedennya = input(promt_text)

        if vvedennya.lower() in ['exit', 'вихід']:
            return 'exit'
        try:
            return float(vvedennya)
        except ValueError:
            print("Помилка: Будь ласка, вводьте лише числа!")

print("Для виходу введіть 'exit' або 'вихід'")
while True:
    x = chisla("Введіть перше число: ")
    if x == 'exit':
        print("Роботу програми завершено.")
        break

    operation = input("Введіть операцію (+, -, *, /): ")
    if operation.lower() in ['exit', 'вихід']:
        print("Роботу програми завершено.")
        break
    
    y = chisla("Введіть друге число: ")
    if y == 'exit':
        print("Роботу програми завершено.")
        break

    result = calc(x, y, operation)
    print(f"Результат: {result}")