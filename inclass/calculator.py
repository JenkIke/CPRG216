class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print("Basic Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        result = calc.add(a, b)
    elif op == '-':
        result = calc.subtract(a, b)
    elif op == '*':
        result = calc.multiply(a, b)
    elif op == '/':
        try:
            result = calc.divide(a, b)
        except ValueError as e:
            print(e)
            exit(1)
    else:
        print("Invalid operation.")
        exit(1)

    print(f"Result: {result}")