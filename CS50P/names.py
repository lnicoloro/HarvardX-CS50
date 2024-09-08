###linear search
import sys

names = ['Charlie', 'Fred', 'Ron']

name = input('Name: ')

if name in names:
    print('found')
    sys.exit(0)

print('Not found')
sys.exit(1)