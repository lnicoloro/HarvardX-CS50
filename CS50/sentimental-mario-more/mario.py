# TODO
def main():
    height = get_height()

    for row in range(height):

        for space in range(height - row - 1):
            print(" ", end="")

        for column in range(row + 1):
            print("#", end="")

        print("  ", end="")

        for column in range(row + 1):
            print('#', end="")

        print()


def get_height():
    while True:
        try:
            i = int(input('Height: '))
            if i > 0 and i < 9:
                return i
        except ValueError:
            print('Enter a Number')



main()