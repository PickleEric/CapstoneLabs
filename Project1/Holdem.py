import DeckofCards
from DeckofCards import Deck
@DeckofCards


class Players:

    def __init__(self):
        self.name = name
        self.hand = []
        self.bet = 0
    
    def draw_hand(self, deck):
        self.hand.append(deck.draw())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()
 
def main():
    
    deck = Deck()
    card = deck.draw()
    card.show()

    
main()