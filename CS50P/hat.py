import random

class Hat:

    houses = ["Gryffindoor", "Hufflepuff", "Ravenclaw", "Slytherine"]

    ## cls is a reference to the class itself
    @classmethod
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))


## accessing a class method inside the class
Hat.sort("Harry")