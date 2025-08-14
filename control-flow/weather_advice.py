# Script to provide clothing advice based on user-inputted weather conditions.

# --- User Input ---
# Prompt the user for the current weather.
# .lower() is used to convert the input to lowercase,
# which makes the comparison case-insensitive (e.g., "Sunny" or "sunny" both work).
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# --- Conditional Logic (Control Flow) ---
# Use if/elif/else to check the weather and provide a recommendation.
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # This block handles any input that doesn't match the expected conditions.
    print("Sorry, I don't have recommendations for this weather.")

