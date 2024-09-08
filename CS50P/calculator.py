
# x = int(input("x: "))
# y = int(input("y: "))

# print(x + y)

# z = x / y
# print(f"{z:.50f}")      ##will print 50 decimals but floating point impercision still a problem

def main():
    x = int(input("What is x? "))
    print("x squared is ", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()