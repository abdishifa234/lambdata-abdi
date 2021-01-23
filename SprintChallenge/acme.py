#part 1 Write a python class

import random

class Product:
    """Class to set Product default attributes
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

# Part 2 Write objects for the above class you created

def stealability(self):
        """This methods prints the product's stealablility"""

        if self.weight / self.price < 0.5:
            print("'Not so stealable...'")
            return
        elif self.weight / self.price >= 0.5 < 1.0:
            print("'Kinda stealable.'")
            return
        else:
            print("'Very stealable!'")
            return

def explode(self):
        """this method prints the product is flammabllity with respect to weight"""

        if self.weight * self.flammability < 10:
            print("'...fizzle'")
            return
        elif self.weight * self.flammability >= 10 < 50:
            print("'...boom!'")
            return
        else:
            print("'...BABOOM!!'")
            return
        pass

#Part 3 Inheritance

class BoxingGlove(Product):
    """class to set Boxing glove parameters.
    """
    def __init__(self, price=10):
        super().__init__(price)

    def explode(self):
        """Prints what will happen if the product is too flammable"""
        print("""\"...it's a glove.\"""")

    def punch(self):
        """Prints what happens when boxing glove punches someone."""
        if self.weight < 5:
            print("'That tickles.'")
            return
        elif self.weight >= 5 < 15:
            print("'Hey that hurt!'")
            return
        else:
            print('\"OUCH!\"')
            return