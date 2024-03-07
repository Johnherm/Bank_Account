# class BankAccount():
#     def __init__(self, initialAmount, acctName):
#         self.balance = initialAmount
#         self.name = acctName
#         print(f"\nAccount'{self.name}' created.")
#         print(f"Balance= ${self.balance:.2f}")


from bank_account import *
import emoji
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Dave.deposit(3000)
Sara.deposit(5000)
Dave.withdraw(100)

Dave.transfer(1000, Sara)
