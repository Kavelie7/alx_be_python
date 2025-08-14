# bank_account.py

class BankAccount:
    """
    A class to represent a simple bank account.

    Attributes:
        __account_balance (float): The balance of the bank account.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional initial balance.

        Args:
            initial_balance (float): The starting balance for the account.
        """
        # Encapsulation is used here by making the attribute private with '__' prefix.
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
            
    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if self.__account_balance >= amount > 0:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        # Print the balance with two decimal places.
        print(f"Current Balance: ${self.__account_balance:.2f}")

