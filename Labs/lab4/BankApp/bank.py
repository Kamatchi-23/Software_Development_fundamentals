"""
1- The Bank class is the main system class
2-Ensure that current balance is $1000, and show the current balance
3- Update the main( ) method in Bank to perform the following actions:
(d) make a deposit (read amount from STDIN)
(w) make a withdraw (read amount from STDIN)
(s) show balance
(x) exit the system
NOTES:
• Handle exceptions related to funds availability in the withdraw action
• The Bank system should offer repeatedly the choices to customers until x is entered
"""

class Bank:
    def __init__(self, balance):
        self.balance = balance
    def viewBalance(self):
        print("Starting Balance: $", self.balance)
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited : $ {amount:.2f}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Amount withdrawn : $ {amount:.2f}")
def main():
    start_balance = 1000
    bank = Bank(start_balance)
    menuopt = input("Start banking (s/w/d/x):")
    while menuopt != 'x':
        match menuopt:
            case 's':
                bank.viewBalance()
            case 'd':
                amount = float(input("Amount to deposit: $"))
                bank.deposit(amount)
            case 'w':
                amount = float(input("Amount to withdraw: $"))
                bank.withdraw(amount)
            case _:
                print("Please enter only s, w, d or x only")
        menuopt = input("Continue banking (s/w/d/x):")
    print("Good-Bye")

if __name__ == "__main__":
    main()