#Banking slot program

def show_balance():
    print("---------------------------------------------------------")
    print(f"Your current balance is: ${balance:.2f}")

def deposite():
    
    amount=float(input("\nEnter the amount to deposite: $"))
    
    if amount<0:
        print("Invalid amount. Please try again.")
        return 0
    else:
        return amount
def withdraw():
    amount=float(input("\nEnter the amount to withdraw: $"))

    if  amount>balance:
        print("Insufficient balance. Please try again.")
        return 0
    elif amount<0:
        print("Invalid amount. Please try again.")
        return 0
    else:
        return amount

balance=0
is_running=True

while is_running:
    print("---------------------------------------------------------")
    print("\nWelcome to the Banking Slot Program")
    print("1. Show Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")

    choice=input("\nEnter your choice (1-4): ")

    if choice=="1":
        show_balance()
    elif choice=="2":
        balance+=deposite()
    elif choice=="3":
        balance-=withdraw()
    elif choice=="4":
        is_running=False
    else:
        print("Invalid choice. Please try again.")

print("\n---------------------------------------------------------")
print("Thank you for using the Banking Slot Program. Goodbye!")