from .show_all import show_all

def player_busts(player, dealer, chips):

    show_all(player, dealer)
    #checking if player value greater than 21 prints "players busts" else prints "players loses"
    if player.value < 21:
        print("So, Player loses!")

    else:
        print("So, Player busts!")
    
    
    chips.bet_lost()