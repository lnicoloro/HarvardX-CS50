def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    integer = d.replace("$", "")
    integer = float(integer)
    return integer

def percent_to_float(p):
    # TODO
    integer = p.replace("%", "")
    integer = float(integer)
    percent = integer / 100
    return percent


main()