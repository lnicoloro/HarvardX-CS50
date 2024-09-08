class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('No Name')
        self.name = name

## by using the parent class as the input the new class will inherit all that parent class's characteristics

class Student(Wizard):
    def __init__(self, name, house):
        ## super() accesses the parent class to then get the name
        super(). __init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super(). __init__(name)
        self.subject = subject


def main():
    student = Student("bob", "home")
    professor = Professor("Bill", "History")
    wizard = Wizard("jpohn")



if __name__ == "__main__":
    main()