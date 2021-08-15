# from Projects.Blackjack.black_subpack import *
import random
from typing import ValuesView

suits = ('Hearts', 'Spades', 'Diamond', 'Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
value = {'Two':2 ,'Three':3,'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
            'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return self.rank + " of " + self.suit



class Deck:
    '''

    '''

    def __init__(self):

        self.full_deck = []

        for suit in suits:
            for rank in ranks:
                self.full_deck.append(Card(suit,rank))

    def shuffle(self):
        return random.shuffle(self.full_deck)

    def deal(self):
       single_card = self.full_deck.pop()
       return single_card
        # b = self.full_deck.pop(0)

        # return [a, b]


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += value[card.rank]

    def clear_hand(self):
        self.cards.clear()

    # def adjust_for_aces(self):
    #     if self.cards[-1].value == 11:
    #         self.cards[-1].value = 1



# class Chips:

#     def __init__(self,total):
#         self.total = total
#         self.bet = 0

#     def bet_won(self):
#         self.total += (self.bet * 1.5) 

#     def bet_lost(self):
#         self.total-=self.bet



# while True:

# cards = Deck()
# cards.shuffle()

# players = hand()
# players.add_card(cards.deal())

# dealers = hand()
# dealers.add_card(cards.deal())

deck = Deck()
deck.shuffle()

player = Hand()
temp = deck.deal()

player.add_card(temp)

print(player.cards)