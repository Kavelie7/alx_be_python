# Script to calculate monthly and projected annual savings with a fixed interest rate.

# --- User Input ---
# Prompt the user to enter their monthly income and convert the input to a float.
# Using float() allows for monetary values with decimal points.
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses and convert the input to a float.
monthly_expenses = float(input("Enter your total monthly expenses: "))

# --- Calculations ---
# Calculate the user's monthly savings.
monthly_savings = monthly_income - monthly_expenses

# Define the annual interest rate as a constant.
ANNUAL_INTEREST_RATE = 0.05

# Calculate the projected savings after one year, including compound interest.
# The formula is (Monthly Savings * 12) + ((Monthly Savings * 12) * Interest Rate).
annual_savings_before_interest = monthly_savings * 12
projected_annual_savings = annual_savings_before_interest + (annual_savings_before_interest * ANNUAL_INTEREST_RATE)

# --- Output Results ---
# Display the user's monthly savings, formatted as a dollar amount.
print(f"Your monthly savings are ${int(monthly_savings)}.")

# Display the projected annual savings, formatted as a dollar amount.
print(f"Projected savings after one year, with interest, is: ${int(projected_annual_savings)}.")

