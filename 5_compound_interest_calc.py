# Compound Interest Calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <= 0:
        print("Principal amount must be greater than 0. Please try again.")

while rate <= 0:
    rate = float(input("Enter the annual interest rate (in %, greater than 0): "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please try again.")

while time <= 0:
    time = float(input("Enter the time in years (greater than 0): "))
    if time <= 0:
        print("Time must be greater than 0. Please try again.")

compound_interest = principal * ((1 + (rate / 100)) ** time) - principal
total_amount = principal + compound_interest

print(f"The compound interest is: {compound_interest:.2f}")
print(f"The total amount is: {total_amount:.2f}")
