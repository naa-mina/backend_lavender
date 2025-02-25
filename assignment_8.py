#fully functional banking system

# Students will build a fully functional ATM system using Python that allows users to:
# ✅ Check their balance
# ✅ Deposit money (No negative deposits)
# ✅ Withdraw money (Check for sufficient balance)
# ✅ View transaction history
# ✅ Use a PIN for security
# ✅ Exit the system


# 📌 Requirements:
# 1. welcome message and action to continue
# 2. enter pin to continue to the ATM- 4 digit pin - numbers only
# 3. Display the menu
# 4. check balance againt an initial balance of 1000.00
# 5. deposit money - no negative deposits      
# 6. Withdraw money -check for sufficient balance
# 7. View transaction history

pin = "1234"
balance = 1000.00
transaction_history = [] #list to store the transactions

def check_balance(balance):
    print(f'Your remaining balance is {balance:.2f}')
    transaction_history.append(f"Checked balance: {balance:.2f}")
    return balance

def deposit_money(balance):
    while True:
        try:
            d_amount = float(input("How much would you like to deposit. \nEnter here: "))
            if d_amount <= 0:
                print("You are trying to deposit an invaild amont")
            else:
                balance = balance + d_amount
                print(f"{d_amount} has been deposited into your account.")
            
                transaction_history.append(f"Deposited {d_amount:.2f}. Your remaining balance is: {balance:.2f}")
                return balance
        except ValueError:
            print("Invalid amount entered. Please enter a valid amount to deposit")

def trans_history():
    if not transaction_history:
        print("No transaction has been made yet!")
    else:
        print("Transaction_history")
        for transaction in transaction_history:
            print(transaction)


def withdraw_money(balance):
    while True:
        try:
            w_amount = float(input("How much would you like to withdraw. \nEnter here: "))

            if w_amount <= 0:
                print("You cannot withdraw less than 0.00 \n Please try again")
                return balance
            elif w_amount > balance:
                print("Insufficient balance \n Please try again")
                return balance
            else: 
                print(f"{w_amount} has been withdrawn from your account.")
                balance = balance - w_amount
                transaction_history.append(f"Withdraw {w_amount:.2f}.Your remaining balance is: {balance:.2f}")
                return balance
        except ValueError:
            print("Invalid amount entered. Please enter a valid amount to withdraw")

def exit_program():
    print("Bye! See you again.")
print("Welcome to the ATM.")

PIN = input("Please enter your pin: ")

while True:
    if PIN != pin :
        print("Invalid Pin. Please try again")
        PIN = input("Please enter your pin: ")
    else:
        menu = '''    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. View Transaction History
    5. Exit the System'''


        print(menu)
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)
            print()
        elif choice == "2":
            balance = deposit_money(balance)
            print()
        elif choice == "3":
            balance = withdraw_money(balance)
            print()
        elif choice == "4":
            trans_history()
            print()
        elif choice == "5":
            exit_program()
            break
        else:
            print("Invalid choice. Please enter between 1 and 5")



