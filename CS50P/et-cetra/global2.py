class Account:
    def __init__(self):
        self._balance = 0

## this getter makes it so only functions within the class can change the value of balance
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print(accout.balance)
    account.deposit(100)
    account.withdraw(5)
    print(account.balance)