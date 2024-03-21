class Account:
    def __init__(self, type):
        self.type = type
        self.balance = self.initBalance()
    def initBalance(self):
        return float(input("Initial balance for your account:"))
    def deposit(self, amount):
        

    