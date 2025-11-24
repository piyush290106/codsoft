def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    valid_ops = {"+", "-", "*", "/", "%", "**"}
    print("\nChoose operation:")
    print("+   -> Addition")
    print("-   -> Subtraction")
    print("*   -> Multiplication")
    print("/   -> Division")
    print("%   -> Modulus")
    print("**  -> Power")

    while True:
        op = input("Enter operation: ").strip()
        if op in valid_ops:
            return op
        print("Invalid operation. Try again.")

def calculate(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            return "Error: Division by zero not allowed."
        return a / b
    if op == "%":
        if b == 0:
            return "Error: Modulus by zero not allowed."
        return a % b
    if op == "**": return a ** b

def main():
    print("=== SIMPLE CALCULATOR ===")
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        op = get_operation()

        result = calculate(num1, num2, op)
        print("Result:", result)

        again = input("\nDo you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
