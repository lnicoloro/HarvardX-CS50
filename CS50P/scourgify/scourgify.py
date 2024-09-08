import sys
import csv

def main():
    command_line()

    students = []

    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            house = row["house"]
            name = row["name"].split(", ")
            first = str(name[1])
            last = str(name[0])
            student = {'first': first, 'last': last, 'house': house}
            students.append(student)


    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})

        for student in students:
            first = student["first"]
            last = student["last"]
            house = student["house"]
            writer.writerow({"first": first, "last": last, "house": house})













def command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV File")



if __name__ == "__main__":
    main()