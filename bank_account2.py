class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"\nAccount '{self.name}' is created with ${self.balance} initial amount")
    #Depositing process
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n{self.name} is added $ {amount}  deposit and now it has $ {self.balance} amount of balance ")
    #Withdrawal process
    def leftBalance(self, left):
        if self.balance >= left:
            return
        else:
            print(f"Sorry your balance is insufficient")
    def withdraw(self, withdraw):
        self.leftBalance(amount)
        self.balance = self.balance - withdraw
        print(f"\n{self.name} is withdraw ${withdraw} and now it has ${self.balance} amount of balance")

