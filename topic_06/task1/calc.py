import function
import operation


def main():
    operation.write_log("Запуск програми")

    a, b = operation.get_numbers()
    op = operation.oper()

    actions = {
        "+": function.plus,
        "-": function.minus,
        "*": function.mnozennia,
        "/": function.dilennia,
    }

    result = actions[op](a, b)
    print(f"Результат: {result}")

    operation.write_log(f"Дані: a={a}, b={b} | Операція: '{op}' | Результат: {result}")
    operation.write_log("Завершення роботи\n")


if __name__ == "__main__":
    main()