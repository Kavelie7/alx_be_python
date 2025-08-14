# Script to create a simple calculator using the match-case statement.

# --- User Input ---
# Prompt the user to enter two numbers. float() is used to allow for decimal values.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation.
operation = input("Choose the operation (+, -, *, /): ")

# --- Match Case Statement ---
# The match statement checks the value of the 'operation' variable.
match operation:
    # If the operation is '+', perform addition.
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    # If the operation is '-', perform subtraction.
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    # If the operation is '*', perform multiplication.
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    # If the operation is '/', handle division with a check for division by zero.
    case "/":
        # Check if the second number is zero before performing the division.
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    # The default case for any other input.
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")

