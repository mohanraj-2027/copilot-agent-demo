"""A simple command-line calculator."""


def is_numeric(value):
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero.")
    return first / second


def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    print("Simple Calculator")
    print("Supported operations: +, -, *, /")

    try:
        first_input = input("First number: ")
        operator = input("Operation: ").strip()
        second_input = input("Second number: ")

        if not is_numeric(first_input) or not is_numeric(second_input):
            print("Please enter numeric values for both numbers.")
            return

        first = float(first_input)
        second = float(second_input)

        if operator not in operations:
            print("Unknown operation.")
            return

        result = operations[operator](first, second)
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
