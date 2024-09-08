## class is like a blue print for a house
class Student:
    ## to initialize the contents of an onject from a class
    ## self gives access to the current object
    def __init__(self, name, house, patronus):
        # if not name:
        #     raise ValueError("Missing Name")
        # if house not in ["Gryffindoor", "Hufflepuff", "Ravenclaw", "Slytherine"]:
        #     raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    ## this function will allow the class to be printed as a string instead of the object's address
    def __str__(self):
        return f"{self.name} from {self.house}"


    def charm(self):
        match self.patronus:
            case "Stag":
                return "horse with antlers"
            case "Otter":
                return "water dog"
            case _:
                return "nothing"

    ## '_' used to differentiate between function and instance variable

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name


    ## Getter (function for a class that gets some attribute)
    @property
    def house(self):
        return self._house

    ## Setter (function for a class that sets some attribute)
    ## this function will be called whenever the attribute is used (student.house)
    @house.setter
    def house(self, house):
        if house not in ["Gryffindoor", "Hufflepuff", "Ravenclaw", "Slytherine"]:
            raise ValueError("Invalid House")
        self._house = house





def main():
    student = get_student()

    ###### editing input
    ## for list
    # if student[0] == 'Joe':
    #     student[1] = 'shack'

    ## for dictionary
    # if student["name"] == "Joe":
    #     student["house"] = "shack"

    ## for tuple or list
    # print(student[0])
    # print(student[1])
    ## for dictionary
    # print(student['name'])
    # print(student['house'])

    ## for  class
    print(student.name)
    print(student.house)
    print(student)
    print(student.charm())




## uses a tuple (collection of values that is imutable aka you cant change the values in a tuple)
## returning only 1 tuple that contains two values
# def get_student():
#     name = input('Name: ')
#     house = input('House: ')
#     return (name, house)

## instead of returning a tuple returns an editable list
# def get_student():
#     name = input('Name: ')
#     house = input('House: ')
#     return [name, house]


## instead using a dictionary to provide keys for each value
# def get_student():
#     name = input('Name: ')
#     house = input('House: ')
#     return {"name": name, "house": house}


def get_student():
    ## an object is like using the class
    name = input('Name: ')
    house = input('House: ')
    patronus = input('Patronus: ')
    ## constructor code, constructs the Student object
    return Student(name, house, patronus)




if __name__ == "__main__":
    main()