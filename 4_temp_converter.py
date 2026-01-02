#Temperature Converter

unit=input("Is the Temperature in Celsius or Fahrenheit? (C/F): ").upper()
temp=float(input("Enter the temperature: "))

if unit=="C":
    converted=(temp*9/5)+32
    print(f"{temp}° Celsius is equal to {converted:.2f}° Fahrenheit.")

elif unit=="F":
    converted=(temp-32)*5/9
    print(f"{temp}° Fahrenheit is equal to {converted:.2f}° Celsius.")

else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


