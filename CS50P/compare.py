# x = int(input("x: "))
# y = int(input("y: "))

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x = y")


# s = input("Do you agree? ")

# if s in ("Y", "y", "yes", "YES"):         ## can express same strings in a list as awell as force all input to lower case
#     print("agree")


# elif s.lower()== "n" or s.lower() == "no":
#     print("disagree")


###########three ways to do the same thing
i = 0
while i < 3:
    print("hi1")
    i += 1

for i in range(3):
    print("hi2")

def hi():
    print("hi3")

for i in range(3):
    hi()


########### can define a main function to not have to use a protytype of a function after it.
def main():     ##main is defined here it will do nothin untill it is called
    hello(3)


def hello(n):            ##hello is defined here it will do nothing till it is called
    for i in range(n):
        print("hello")

main()      ##main wont do anything untill it is called here


s = input('s: ')
t = input('t: ')

if s == t:
    print("Same")
else:
    print('different')

t = s.capitalize()          ####will only capitalize the first letter
print(t)



#####swapping

x = 1
y = 2

print(f"x: {x}, y: {y}")

x, y = y, x

print(f"x: {x}, y: {y}")