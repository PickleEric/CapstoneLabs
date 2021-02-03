from dataclasses import dataclass
import random
from random import shuffle 

@dataclass
# create card
class Card:
    value: str
    suit: str

    def show(self):
        print(f'{self.suit} of {self.value}')
# build a deck, 52 cards, Jack, Queen, King, Ace = 11
class Deck:
    def __init__(self):
        self.cards = [] 
        self.create()

    def create(self): 
        for s in ['Hearts', 'Clubs', 'Diamonds', 'Hearts']:
            for v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(v, s))
# shuffle the deck with random shuffle
    def shuffle(self): 
        for i in self.cards:
            shuffle(self.cards) 
    
    def draw(self):
        return self.cards.pop()


