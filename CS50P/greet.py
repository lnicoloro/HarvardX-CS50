from sys import argv

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print('hello')

for arg in argv:
    print(arg)

for arg in argv[1:2]:       ##slice a list to print only certain parts
    print(arg)

import sys

if len(sys.argv) != 2:
    print("Mising argument")
    sys.exit(1)

print(f'hello, {sys.argv(1)}')  ##printing the second element in argv

sys.exit(0)