# name = input("What is your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
## a appends to the file instead of overwrite it



# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello, ", line.rstrip())
## rstrip removes \n from test file



names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello {name}")
## create a list to sort names and then print by alpha



# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello, " line.rstrip())
## sorts the actual file