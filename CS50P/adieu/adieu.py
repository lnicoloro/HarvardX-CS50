import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input('Name: ')
        names.append(name)
    except EOFError:
        people = p.join(names)
        print(f'\nAdieu, adieu, to {people}')
        break