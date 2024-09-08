import sys

def main():
    command_line()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")


    count = 0
    for line in lines:
        if line_check(line) == False:
            count += 1

    print(count)



def command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python File")



def line_check(line):
    if line.isspace():
        return True
    elif line.lstrip().startswith("#"):
        return True

    return False



if __name__ == "__main__":
    main()