class BankAccount:
    # don't forget to add some default values for these parameters!
    balance = 0
    int_rate = 0
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.02,0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def userBalance(self):
        self.account.display_account_info()
        return self


todd = BankAccount(.01,100)
ted = BankAccount(.02,1000)

todd.deposit(50).deposit(50).deposit(100).withdraw(50).yield_interest().display_account_info()

ted.deposit(100).deposit(100).withdraw(200).withdraw(200).withdraw(200).withdraw(1000).yield_interest().display_account_info()

