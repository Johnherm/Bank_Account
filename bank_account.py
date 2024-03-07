class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        #Creating bank account with initial amount
        print(f"\nAccount'{self.name}' created.")
        print(f"Balance= ${self.balance:.2f}")
        #Show account name with balance
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = $'{self.balance:.2f}'")
        #Adding more balance to the initial balance as a deposit
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nAccount '{self.name}' balance = $'{self.balance:.2f}'")
        print("Deposit complete")
        #Checking left amount of balance to withdraw
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n Sorry, account'{self.name}' only has a balance of $'{self.balance:.2f}'")
    #Withdraw 
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdraw complete\n Your left balance is :{self.balance}")
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")
