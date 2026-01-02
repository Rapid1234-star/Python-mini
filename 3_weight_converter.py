#Weight Converter

weight=float(input("Enter weight: "))
unit=input("Enter unit (L for pounds, K for kilograms): ").upper()

if unit=='K':
    converted=weight*2.20462
    print(f"{weight} kilograms is equal to {converted:.2f} pounds.")

elif unit=='L':
    converted=weight/2.20462
    print(f"{weight} pounds is equal to {converted:.2f} kilograms.")
     
else:
    print("Invalid unit. Please enter 'L' for pounds or 'K' for kilograms.")
