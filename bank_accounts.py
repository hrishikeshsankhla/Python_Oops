class BalanceException(Exception):
   pass



class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created .\nBalance = ${self.balance: }")

    def getBalance(self):
        print(f"\nAccount '{self.name} balance = $ {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited ${amount} into account '{self.name}'.")
        print(f"Account '{self.name}' balance = ${self.balance}")

    def viableTransaction (self, amount):
        if self.balance>=amount:
            return 
        else:
            raise BalanceException(
                f"\n Sorry, '{self.name}' only has balance of {self.balance}"
                )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\n Withdraw Complete.")
            self.getBalance()

        except BalanceException as error:
            print(f"\n Withdraw Interrupted : {error}")


    def transfer(self, amount, account):
        try:
            print("\n **********\n\n Beginning Transfer")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n Transfer Complete\n\n**********")
        except BalanceException as error:
            print(f"\n Transfer Interrupted : {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\nDeposited ${amount} into account '{self.name}'.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee=5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw Interrupted : {error}")
            
