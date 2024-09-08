#dictionary contains keys and values; in this case names and numbers
# one syntax is people = dict()

people = {
    'Carter': '12345',
    'David': '54321'
}

name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")



#######code to add to phonebok.csv

import csv

with open("phonebook.csv", "a") as file:       ##opens file in append mode and will close it after the folling code is exicuted

    name = input('Name: ')
    number = input('Number: ')

    writer = csv.DictWriter(file, fieldnames = ["name", "number"])  #will creat a dictionary to keep names and numbers in the right columns
    writer.writerow(["name": name, "number": number])               #associates name and number with correct variables
