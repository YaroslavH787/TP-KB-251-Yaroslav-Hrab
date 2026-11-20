import functions
import operation

def main():
    a, b = operation.get_number()
    op = operation.oper()

    action = {
        "+": functions.plus,
        "-": functions.minus,
        "*": functions.mnozennia,
        "/": functions.dilennia,
    }

    result = action[op](a, b)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()