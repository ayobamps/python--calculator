
# Python Calculator

def calculator():
    print("Welcome to My Python Calculator!")

    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print("Result:", result)


calculator()
