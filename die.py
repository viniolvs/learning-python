#rola um dado 

from random import randint

class Die():
    def __init__(self,sides) -> None:
        if (sides <= 6 ):
            self.sides = 6
        else: 
            self.sides = sides
    def rollDie(self):
        rolled_number = randint(1, self.sides)
        print("Rolled number: ", rolled_number)

d = Die(6)
d.rollDie()