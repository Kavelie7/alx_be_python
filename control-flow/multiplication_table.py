# Script to generate a multiplication table for a number provided by the user.

# --- User Input ---
# Prompt the user to enter a number and convert the input to an integer.
# int() is used because we're dealing with whole numbers for a multiplication table.
number = int(input("Enter a number to see its multiplication table: "))

# --- For Loop to Generate Table ---
# The for loop iterates through a sequence of numbers from 1 to 10.
# The range(1, 11) function generates numbers from 1 up to (but not including) 11.
for i in range(1, 11):
    # Calculate the product of the user's number and the current number in the loop.
    product = number * i
    # Print the result in the specified format.
    print(f"{number} * {i} = {product}")

