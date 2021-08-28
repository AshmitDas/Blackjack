from .show_all import show_all

def dealer_Wins(player, dealer, chips):

        show_all(player,dealer)
        print("So, Dealer wins.\n")
        chips.bet_lost()