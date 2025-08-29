"""
A class representing a simple bank account.

Attributes:
    owner (str): The name of the account owner.
    balance (float): The current balance of the account.
    transactions (list): A list of all final balances after each transaction.

Methods:
    deposit(amount):
        Deposits a positive amount into the account.
        Returns True if the deposit is successful, otherwise False.
    withdraw(amount):
        Withdraws a positive amount from the account if sufficient funds exist.
        Returns True if the withdrawal is successful, otherwise False.
    get_balance():
        Returns the current account balance.
    update_transactions():
        Appends the current balance to the transactions list.
    __str__():
        Returns a string representation of the BankAccount instance.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            owner (str): The name of the account owner.
            balance (float, optional): The initial balance of the account. Defaults to 0.
        """
        self.owner = owner
        self.balance = balance
        self.transactions = [self.balance]

    def deposit(self, amount):
        """
        Deposits a positive amount into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            bool: True if the deposit is successful, otherwise False.
        """
        if amount > 0:
            self.balance += amount
            self.update_transactions()
            return True
        return False

    def withdraw(self, amount):
        """
        Withdraws a positive amount from the account if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal is successful, otherwise False.
        """
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            self.update_transactions()
            return True
        return False

    def get_balance(self):
        """
        Returns the current account balance.

        Returns:
            float: The current balance of the account.
        """
        return self.balance

    def update_transactions(self):
        """
        Appends the current balance to the transactions list.
        """
        self.transactions.append(self.balance)

    def __str__(self):
        """
        Returns a string representation of the BankAccount instance.

        Returns:
            str: String representation of the BankAccount.
        """
        return f"BankAccount(owner={self.owner}, balance={self.balance})"