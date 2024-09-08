


class Dog:
    _name = None

    def __init__(self, breed, color):
        self._breed = breed
        self._color = color

    def GetName(self):
        if (self._name == None):
            self._name = "Dog"

        return self._name

    def __str__(self):
        return "This is " + self._name + ". A " + self._color + " " + self._breed + "."

    def Greet(self, other):
        print(self._name + " greets " + other._name + ".")


def main():

    myDog = Dog("Golden Retriever", "Red")
    myDog._name = "Rex"

    dogString = str(myDog)
    print(dogString)

    print(myDog)

    otherDog = Dog("Lab", "Yellow")
    otherDog.GetName()
    myDog.Greet(otherDog);

main()