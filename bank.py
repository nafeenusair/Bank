def show_balance(balance):
    print(f"Your current balance is: {balance}")

def deposit(balance):
    deposit_value = float(input("Enter the amount you'd like to deposit: "))
    balance += deposit_value
    print("Money deposit successful")
    return balance

def withdraw(balance):
    withdraw_value = float(input("Enter the amount you'd like to withdraw: "))
    balance -= withdraw_value
    print("Money withdraw successful")
    return balance

is_running = True
bank_balance = float(input("What is your initial balance: "))

print("*******************")
print("  Banking Program  ")
print("*******************")

while is_running:
    print("1. Bank Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*******************")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            show_balance(bank_balance)
        case 2:
            bank_balance = deposit(bank_balance)
        case 3:
            bank_balance = withdraw(bank_balance)
        case 4:
            print("Thank you for using our bank")
            is_running = False
        case _:
            print("invalid input")