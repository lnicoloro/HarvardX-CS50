balance = 0
## can read from global variable anywhere
## can not write to a global variable from anywhere
## informing functions balance is gloabl allows them to edit it

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n



if __name__ == "__main__":
    main()