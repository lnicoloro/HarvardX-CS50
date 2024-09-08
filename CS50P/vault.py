class Vault:
    def __init__(self, quarters=0, dimes=0, pennies=0):
        self.quarters = quarters
        self.dimes = dimes
        self.pennies = pennies

    def __str__(self):
        return f"{self.quarters} quaters, {self.dimes} dimes, {self.pennies} pennies"

    def __add__(self, other):
        quarters = self.quarters + other.quarters
        dimes = self.dimes + other.dimes
        pennies = self.pennies + other.pennies
        return Vault(quarters, dimes, pennies)



def main():
    potter = Vault(100, 50, 10)
    print(potter)

    weasly = Vault(50, 25, 5)
    print(weasly)

    # quarters = potter.quarters + weasly.quarters
    # dimes = potter.dimes + weasly.dimes
    # pennies = potter.pennies + weasly.pennies
    # combined = Vault(quarters, dimes, pennies)
    # print(combined)

    combined = potter + weasly
    print(combined)





if __name__ == "__main__":
    main()