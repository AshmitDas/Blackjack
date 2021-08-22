def show_some(player,dealer):

    #Show dealers card
    print("\nDealer's Hand: \nFirst Card Hidden!")
    print(dealer.cards[1])

    #show players card
    print("Player's Hand: ")
    for card in player.cards:
        print(card)