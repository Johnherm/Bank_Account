class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"\nAccount '{self.name}' is created with ${self.balance} initial amount")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.name} is added $ {amount}  deposit and now it has $ {self.balance} amount of balance ")
