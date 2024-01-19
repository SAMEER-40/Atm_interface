# ATM System Project
Overview
This project implements a simple ATM system using Python.
The system allows users to create accounts, log in, and perform various operations such as checking balance, withdrawing money, depositing money, transferring funds, and viewing transaction history.

Classes
User
- __init__(self, user_id, pin, balance=0): Initializes a User object with a unique user ID, PIN, and an optional starting balance.
- display_balance(self): Displays the current balance of the user.
- withdraw(self, amount): Withdraws funds from the user's account. Returns a message indicating the success or failure of the withdrawal.
- deposit(self, amount): Deposits funds into the user's account. Returns a message indicating the success or failure of the deposit.
- transfer(self, target_account, amount): Transfers funds to another user's account. Returns a message indicating the success or failure of the transfer.

ATMSystem
-1.__init__(self): Initializes the ATMSystem with an empty user dictionary and a variable to track the current user.
-2.create_account(self): Creates a new user account by generating a user ID and taking a PIN as input.
-3.authenticate_user(self, user_id, pin): Authenticates the user by checking the user ID and PIN.
-4.run_atm(self): Main function to run the ATM system, offering options for account creation, login, and operations.
-5.perform_operations(self): Function to perform ATM operations after successful login.

Usage
-1.Run the program by executing the Python script: python main.py.
-2.Follow the on-screen instructions to open an account, log in, and perform various ATM operations.
-3.Enjoy the basic functionalities of the ATM system!

Note
-This project is a simple implementation for educational purposes. In a real-world scenario, additional security measures and error handling would be necessary.
