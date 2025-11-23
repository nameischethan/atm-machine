import time

ACCOUNTS = {
    '1234567890': {'pin': '1111', 'balance': 15008.75, 'name': 'Salaar'},
    '1357924680': {'pin': '2222', 'balance': 500864.00, 'name': 'Ojas Ghambheera'},
    '2468013579': {'pin': '3333', 'balance': 1234795.67, 'name': 'AVR Mayuri'},
    '1030507090': {'pin': '4444', 'balance': 807.50, 'name': 'M. Sai Charan'},
    '2040608000': {'pin': '5555', 'balance': 99993.99, 'name': 'T. Mohit '}
}


def check_credentials(account_num, pin):
    if account_num in ACCOUNTS:
        if ACCOUNTS[account_num]['pin'] == pin:
            return True, "Success"
        else:
            return False, "Error: Invalid PIN."
    else:
        return False, "Error: Account number not found."

def check_balance(account_num):
    balance = ACCOUNTS[account_num]['balance']
    print(f"\nAccount Holder: {ACCOUNTS[account_num]['name']}")
    print(f"Current Balance: ${balance:,.2f}")
    time.sleep(1) 

def deposit(account_num):
    while True:
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("Deposit amount must be positive.")
                continue
            
            ACCOUNTS[account_num]['balance'] += amount
            print(f"\nDeposit successful! ${amount:,.2f} added.")
            check_balance(account_num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def withdraw(account_num):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: $"))
            balance = ACCOUNTS[account_num]['balance']
            
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                continue
            
            if amount > balance:
                print(f"Insufficient Funds! Available: ${balance:,.2f}")
                continue

            if amount > 1000:
                print("Withdrawal limit exceeded. Maximum withdrawal is $1000.")
                continue
                
            ACCOUNTS[account_num]['balance'] -= amount
            print(f"\nWithdrawal successful! Please take your cash: ${amount:,.2f}")
            check_balance(account_num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def reset_pin(account_num):
    while True:
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            ACCOUNTS[account_num]['pin'] = new_pin
            print(f"\nPIN successfully reset for account {account_num}!")
            time.sleep(1)
            break
        else:
            print("Invalid PIN. PIN must be exactly 4 digits.")

def atm_interface():
    print("       Welcome to the ATM       ")
    max_attempts = 3
    for attempt in range(max_attempts):
        account_num = input("Enter Account Number: ").strip()
        pin = input("Enter PIN: ").strip()

        is_valid, message = check_credentials(account_num, pin)
        
        if is_valid:
            print(f"\nAccess Granted! Hello, {ACCOUNTS[account_num]['name']}!")
            break
        else:
            print(f"\n{message}")
            if attempt < max_attempts - 1:
                print(f"Attempts remaining: {max_attempts - 1 - attempt}\n")
            else:
                print("Too many failed attempts. Card retained. Goodbye.")
                time.sleep(2)
                return 
    else:
        return

    while True:
        print("          ATM Main Menu              ")
        print("1. Account Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Reset PIN")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            check_balance(account_num)
        elif choice == '2':
            deposit(account_num)
        elif choice == '3':
            withdraw(account_num)
        elif choice == '4':
            reset_pin(account_num)
        elif choice == '5':
            print("\nThank you for using the Python ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":

    atm_interface()
