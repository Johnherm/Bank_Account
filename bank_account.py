class BankAccount():
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount'{self.name}' created.")
        print(f"Balance= ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = $'{self.balance:.2f}'")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nAccount '{self.name}' balance = $'{self.balance:.2f}'")
        print("Deposit complete")