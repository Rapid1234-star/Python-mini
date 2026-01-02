#Concession

menu={"pizza":10,
      "burger":8,
      "pasta":12,
      "salad":7,
      "soda":3,
      "water":2,
      "ice Cream":5}

cart=[]

total=0

for key,value in menu.items():
    print(f"{key:<12}: ${value:.2f}")

print("------------------------")

while True:
    food=input("Select a food item to add to your cart (or q to quit): ").lower()

    if food.lower()=="q":
        break
    elif food in menu:
        cart.append(food)
        total+=menu[food]
        print(f"{food} added to cart.")
    else:
        print("Invalid food item. Please try again.")

print("\nYour Cart:")
for item in cart:
    print(f"- {item}: ${menu[item]:.2f}")
print(f"\nTotal Amount: ${total:.2f}")