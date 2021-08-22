def show_all(player,dealer):

    #show dealers hand
    print("Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    
    #value of dealers hand
    print(f"Value of Dealer's hand {dealer.value}")

    #show players hand
    print("Player's Hand: ")
    for card in player.cards:
        print(card)

    #value of players hand
    print(f"Value of Player's hand is {player.value}")