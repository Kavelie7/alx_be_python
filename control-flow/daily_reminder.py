# Script to provide a customized daily task reminder based on priority and time sensitivity.

# --- User Input ---
# Prompt the user for the task description.
task = input("Enter your task: ")

# Prompt for the task's priority (high, medium, low) and convert to lowercase for consistent matching.
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound (yes or no) and convert to lowercase.
time_bound = input("Is it time-bound? (yes/no): ").lower()

# --- Process Task and Provide Reminder ---
# Initialize an empty string for the reminder message.
reminder_message = ""

# Use a match-case statement to handle different priority levels.
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder_message = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task"
    case _:
        # Default case for invalid priority input.
        reminder_message = f"Reminder: '{task}' has an unknown priority"

# Modify the reminder if the task is time-bound.
if time_bound == "yes":
    # Append the immediate attention phrase if time-bound.
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no":
    # Add a suggestion for non-time-bound tasks, regardless of initial priority, as per example.
    # We'll adjust the message based on the initial reminder.
    if "high priority" in reminder_message or "medium priority" in reminder_message:
        reminder_message += ". Consider completing it soon."
    elif "low priority" in reminder_message:
        reminder_message += ". Consider completing it when you have free time."
    else: # For unknown priority but not time-bound
        reminder_message += ". No immediate action required."
else:
    # Handle invalid input for time_bound
    reminder_message += ". (Time-bound status unclear)."

# --- Output the Reminder ---
print(reminder_message)