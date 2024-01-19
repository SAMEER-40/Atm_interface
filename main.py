import random
import string


class User:
    def __init__(self, user_id, pin, balance=0):
        """
        Initialize a User object with a unique user ID, PIN, and an optional starting balance.
        """
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []  # List to store transaction history

    def display_balance(self):
        """
        Display the current balance of the user.
        """
        return f"Your current balance is ${self.balance}"

    def withdraw(self, amount):
        """
        Withdraw funds from the user's account. Returns a message indicating the success or failure of the withdrawal.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrawal successful. {self.display_balance()}"
        else:
            return "Invalid amount or insufficient funds."

    def deposit(self, amount):
        """
        Deposit funds into the user's account. Returns a message indicating the success or failure of the deposit.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposit successful. {self.display_balance()}"
        else:
            return "Invalid amount for deposit."

    def transfer(self, target_account, amount):
        """
        Transfer funds to another user's account. Returns a message indicating the success or failure of the transfer.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {target_account.user_id}")
            return f"Transfer successful. {self.display_balance()}"
        else:
            return "Invalid amount or insufficient funds for transfer."


def generate_user_id():
    """
    Generate a random user ID consisting of lowercase letters and digits.
    """
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(8))


class ATMSystem:
    def __init__(self):
        """
        Initialize the ATMSystem with an empty user dictionary and a variable to track the current user.
        """
        self.users = {}
        self.current_user = None

    def create_account(self):
        """
        Create a new user account by generating a user ID and taking a PIN as input.
        """
        user_id = generate_user_id()
        pin = input("Enter your PIN: ")
        self.users[user_id] = User(user_id, pin)
        print(f"Account created successfully! Your User ID is: {user_id}")

    def authenticate_user(self, user_id, pin):
        """
        Authenticate the user by checking the user ID and PIN.
        """
        if user_id in self.users and pin == self.users[user_id].pin:
            self.current_user = self.users[user_id]
            return True
        else:
            return False

    def run_atm(self):
        """
        Main function to run the ATM system, offering options for account creation, login, and operations.
        """
        print("Welcome to the ATM System!")

        while True:
            print("\nSelect Operation:")
            print("1. Open Account")
            print("2. Log In")
            print("3. Quit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                user_id = input("Enter your User ID: ")
                pin = input("Enter your PIN: ")
                if self.authenticate_user(user_id, pin):
                    self.perform_operations()
                else:
                    print("Authentication failed. Please check your User ID and PIN.")
            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def perform_operations(self):
        """
        Function to perform ATM operations after successful login.
        """
        while True:
            print("\nSelect Operation:")
            print("1. Display Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. View Transaction History")
            print("6. Log Out")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                print(self.current_user.display_balance())
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                print(self.current_user.withdraw(amount))
            elif choice == "3":
                amount = float(input("Enter deposit amount: "))
                print(self.current_user.deposit(amount))
            elif choice == "4":
                target_id = input("Enter target user ID for transfer: ")
                amount = float(input("Enter transfer amount: "))
                if target_id in self.users:
                    target_user = self.users[target_id]
                    print(self.current_user.transfer(target_user, amount))
                else:
                    print("Target user not found.")
            elif choice == "5":
                print("\nTransaction History:")
                for transaction in self.current_user.transaction_history:
                    print(transaction)
            elif choice == "6":
                print("Log out successful. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


# Run the ATM System
atm_system = ATMSystem()
atm_system.run_atm()
