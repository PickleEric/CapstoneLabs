import random

class Dice:
    def __init__(self, sides=6): # first comprehension 
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides) # random in will be created depending on the sides of dice

def main():

    dice = Dice() # 6 sidded die

    print(dice.roll())

    d20 = Dice(20) # 20 sidded

    for r in range(10):
        print(d20.roll())
        
main()