# Script to draw a square pattern of asterisks using nested loops.

# --- User Input ---
# Prompt the user to enter a positive integer for the pattern size.
# int() is used to convert the input to a number.
size = int(input("Enter the size of the pattern: "))

# --- Pattern Drawing Logic ---
# Initialize a counter for the rows.
row = 0

# The while loop continues as long as the row counter is less than the desired size.
while row < size:
    # The nested for loop handles printing the asterisks for each column in the current row.
    # It iterates 'size' number of times.
    for column in range(size):
        # The 'end=""' argument prevents the print function from adding a newline,
        # so the asterisks are printed side by side.
        print("*", end="")

    # After the inner for loop completes (i.e., after one full row is printed),
    # this print() statement adds a newline character to move to the next row.
    print()

    # Increment the row counter to move to the next row.
    row += 1

