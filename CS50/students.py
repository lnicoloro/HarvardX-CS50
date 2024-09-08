# with open("students.csv") as file:
#     for line in file:
#         ## split() returns a list
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")




# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]


# def get_house(student):
#     return student["house"]

## functions will return either the house or name of given student
## functions give the string that the sorted function will use to sort
## key is used tells python what to sort by

# for student in sorted(students, key=get_house):
#     print(f"{student['name']} is in {student['house']}")

## create a list of with a dictionary for each student
## sort by looking a value for each student's dictionary (name)

## can use lamba function instead to creat anonymous function

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")


## same as above but can split better if a value in the csv contains a "," using reader
## reader returns a list
# import csv
# students = []
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, house, home in reader:
#         students.append({"name": name, "house": house, "home": home})
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

## using DictReader
## DictReader returns dictionaries
## must include titles inteh csv files
# import csv
# students = []
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "house": row["house"], "home": row["home"]})
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")




## write csv
# import csv

# name = input("Name: ")
# house = input("House: ")
# home = input("Home: ")

# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=['name', 'house', 'home'])
#     writer.writerow({"name": name, "house": house, "home": home})