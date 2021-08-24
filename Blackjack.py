# from Projects.Blackjack.black_subpack.push import push
# from Projects.Blackjack.black_subpack.dealer_busts import dealer_busts
# from Projects.Blackjack.black_subpack.player_wins import player_win
# from Projects.Blackjack.black_subpack.player_busts import player_busts
# from Projects.Blackjack.black_subpack.hit_or_stand import hit_or_stand
# from Projects.Blackjack.black_subpack.show_some import show_some
# from Projects.Blackjack.black_subpack.take_bet import take_bet
# from Projects.Blackjack.black_subpack.take_hit import take_hit
# from Projects.Blackjack.black_subpack import *
import black_subpack as black
import random

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


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += value[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def clear_hand(self):
        self.cards.clear()

    def adjust_for_aces(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    #     if self.cards[-1].value == 11:
    #         self.cards[-1].value = 1



class Chips:

    def __init__(self,total):
        self.total = total
        self.bet = 0

    def bet_won(self):
        self.total += self.bet

    def bet_blackjack(self):
        self.total += (self.bet * 1.5)

    def bet_lost(self):
        self.total-=self.bet

while True:

    print("Welcome to Blackjack/21 Game.\nThis a purely Terminal based game.")

    deck = Deck() #Creating a deck object of the class Deck
    deck.shuffle() #Shuffling the deck of cards

    players_hand = Hand()
    dealers_hand = Hand()

    for _ in range(2):
        black.take_hit(players_hand,deck)
        black.take_hit(dealers_hand,deck)

    # Prompting player to enter total amount 
    total_amount = int(input("Enter the total amount of money to place: "))
    players_chip = Chips(total_amount)


    #Taking players bet amount
    black.take_bet(players_chip)

    #showing players all cards and dealers second card
    black.show_some(players_hand,dealers_hand)

    while True:

        #Asking player if he/she want to stand or hit
        black.hit_or_stand(players_hand,deck)

        #show all the cards of players hand but keeping one card hidden in dealers hand
        black.show_some(players_hand,dealers_hand)

        #if players hand exceeds 21, calling player_busts function and breaking out of the loop
        if players_hand.value > 21:

            black.player_busts(players_hand,dealers_hand,players_chip)
            break

        #If players hand is equal to 21, Its a blackjack, callng function player_win and breaks out of the loop
        elif players_hand.value == 21:

            print("Its a Blackjack!")
            black.player_win(players_hand,dealers_hand,players_chip)
            break

        else:

            #if dealers value is less than 17, adding card to dealers hand until its equal to 17 or greater than that
            while dealers_hand.value < 17:

                black.take_hit(dealers_hand,deck)

            
            #If dealers value exceeds 21, player wins and breaks out of the loop
            if dealers_hand.value > 21:

                black.dealer_busts(players_hand, dealers_hand, players_chip)
                break

            #if players value exceeds that of dealer, calling player_win function
            elif players_hand.value > dealers_hand.value:
                
                black.player_win(players_hand, dealers_hand, players_chip)
                break

            #if dealers value exceeds players value, player loses
            elif dealers_hand.value > players_hand.value:

                black.player_busts(players_hand, dealers_hand, players_chip)
                break

            #if dealers value is equal to that of players value
            else:

                black.push()
                break

        
    play_again = input("Do you want to play again? \nType 'y' or 'n': ")

    if play_again[0].lower() == 'y':
        continue

    else:

        print("Thank you for playing!")
        break
