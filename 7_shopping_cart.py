foods=[]
prices=[]
total=0

while True:
    food=input("Enter a food item to buy (or q to quit): ")

    if food.lower()=="q":
        break

    else:
        price=float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
        total+=price

print("\nYour Shopping Cart:")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")

print(f"\nTotal: ${total:.2f}")