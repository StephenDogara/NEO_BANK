from account import Account

class currentaccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount