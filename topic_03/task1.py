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

print("Для виходу введіть 'exit' або 'вихід' під час введення першого числа.\n")

while True: 
      vvedenya = input("Введіть перше число: ")

      if vvedenya.lower() in ['exit', 'вихід']:
            print("Роботу програми завершено.")
            break

      try:
            x = float(vvedenya)
            operation = input("Введіть операцію (+, -, *, /): ")
            y = float(input("Введіть друге число: "))
            result = calc(x, y, operation)
            print(f"Результат: {result}") 
      except ValueError:
            print("Помилка: Будь ласка, вводьте лише числа!")