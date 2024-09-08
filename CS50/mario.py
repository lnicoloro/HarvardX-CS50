
def main():
    height = get_height()
    for i in range(height):
        print("#")

    length = get_length()
    for j in range(length):
        print("#", end="")       ####changes the end of a line form \n to nothing so it wont start on a new line

    print()                         ###moves cursor to next line




def get_height():
    while True:                  ######python version of a do while loop
        try:                    ###### python will try this unless there is an error in this case cause by input of a string and not an int
            x = int(input("Height: "))
            if x > 0:
                return x
        except ValueError:
            print("Please Type A Number")
                #### x will exist outside the loop it was defined in python lets it be used anytime after it is defined



def get_length():
        while True:
            try:
                x = int(input("Length: "))
                if x > 0:
                    return x
            except ValueError:
                print("Please Type A Number")


main()

#print("!" * 5)      ## can also just multiply strings


#############print a 2D shape

for i in range(3):
    for j in range(3):
        print("#", end="")
    print()