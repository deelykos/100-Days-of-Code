#!/usr/bin/env python3


# Create a welcome message
print("Welcome to the tip calculator!")

# Ask the user for the total bill
total_bill = float(input("What was the total bill? $"))

# Ask for user tip to give
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
tip_percentage = tip / 100
tip_amount = tip_percentage * total_bill

# Amount of people to split the bill
spilt_bill = int(input("How many people to split the bill?"))

# Amount each person should pay
each_bill = total_bill + tip_amount
each_bill_total = round(each_bill / 7, 2)

# Print the amount each person should pay
print(f"Each person should pay: ${each_bill_total}")