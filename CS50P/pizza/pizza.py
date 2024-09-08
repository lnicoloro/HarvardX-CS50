import sys
import csv
from tabulate import tabulate

def main():
    command_line()
    pizza = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                pizza.append(row)
            print(tabulate(pizza[1:], headers = pizza[0], tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")



def command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV File")



if __name__ == "__main__":
    main()