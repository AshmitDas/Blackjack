from .show_all import show_all

def player_win(player, dealer, chips):

    show_all(player, dealer)
    print("so, Players wins!\n")
    chips.bet_won()