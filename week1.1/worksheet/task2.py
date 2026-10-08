"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
while True:
    monthly_input = input("How much are you willing to save every month? ").strip()
    try:
        monthly_amount = int(monthly_input)
        if monthly_amount < 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid amount")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
annual_savings = monthly_amount * 12
print(f"By the end of the year, you will have saved £{annual_savings}.")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
interest = annual_savings * 0.008
total_with_interest = annual_savings + interest

print(f"After interest, your total savings will be £{total_with_interest:.2f}")
