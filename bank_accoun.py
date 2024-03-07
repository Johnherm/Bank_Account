class BankAccount():
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount'{self.name}' created.")
        print(f"Balance= ${self.balance:.2f}")