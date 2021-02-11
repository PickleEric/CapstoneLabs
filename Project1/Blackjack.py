from dataclasses import dataclass
import random
from random import shuffle 
#Only runs when you do not have a value of jack, queen, king, or ace 
#
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
# Create Player and dealer hand
class Hand:
    # Unless it is dealer this will be false allowing the player to draw
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards =[]
        self.value = 0 # add value to cards in hand

    def add_card(self, card):
        self.cards.append(card)

    def calc_value(self):
        self.value = 0

        has_ace = False
        for card in self.cards:
            if card.value:
                self.value += int(card.value)
            else:
                # make case for the ACE = 11
                if card.value == "Ace": 
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 1
                if card.value == "King" or "Queen" or "Jack": # Apply value to facecards -- this is not working
                    self.value += 10
                else:
                    self.value += 1
        if has_ace and self.value > 21:
            self.value += 11

    def get_value(self):
        self.calc_value() # store our value
        return self.value
        #show dealer hand
    def display(self):
        if self.dealer:
            print('hide')
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print('Value: ', self.get_value())
            
class Table:
    def __inti__(self):
        pass
    
    def play(self):
        playing = True
        #Create game loop
        while playing:
            # call the deck 
            self.deck = Deck() 
            # shuffle the deck
            self.deck.shuffle()
            # create payer hand and dealer hand
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer = True)
            # only allow 2 in the range
            for i in range(2): 
            
                self.player_hand.add_card(self.deck.draw())
                self.dealer_hand.add_card(self.deck.draw())
            print('Player Hand: ')

            self.player_hand.display()
            print()
            print('Dealer Hand: ')
            
            self.dealer_hand.display()
            # create the game to ask hit or stay
            choice = input('Hit or Stay?')
            while choice not in ['hit', 'stay']:
                choice = input('what would you like to do?')
            if choice in ['hit']:
                self.player_hand.add_card(self.deck.draw())
                self.player_hand.display()
            else:
                player_hand_value = self.player_hand.get_value()
                dealer_hand_value = self.dealer_hand.get_value()

                print('Final Result')
                print('You have: ', player_hand_value)
                print('Dealer has: ', dealer_hand_value)

                if player_hand_value > dealer_hand_value:
                    print("WINNER")
                elif player_hand_value == dealer_hand_value:
                    print('Draw')
                else:
                    print('Dealer Wins')
                game_end = True
            if self.play_is_over():
                print('You lose!')
                game_end = True

        game_end = False
        while not game_end:
            # call who the winner is
            self.player_has_blackjack, self.dealer_has_blackjack = self.check_for_winner() 
        # creat play again input
        again = input('Play again? (Y/N) ')
        while again.lower() not in ['y', 'n']:
            again = input('Yes or No?')
        if again.lower() == 'n':
            print('Good Bye!')
            playing = False
        else:
            game_end = False
        # check who won by comparing to 21
    def check_for_winner(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        if self.player_has_blackjack or self.dealer_has_blackjack:
            game_end = True
        self.show_results(self.player_has_blackjack, self.dealer_has_blackjack)
        return player, dealer
        
    # Show the results 
    def show_results(self):

        if self.player_has_blackjack and self.dealer_has_blackjack:
            print('DRAW!')
        elif self.player_has_blackjack:
            print('You are winner!')
        elif self.dealer_has_blackjack:
            print('You lose!')
        
    def game_end(self): # end game this does not run
        return self.player_hand.get_value() > 21
# call MAIN
if __name__ == '__main__':
    table = Table()
    table.play()