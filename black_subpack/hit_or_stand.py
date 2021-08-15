def hit_or_stand(player,deck):

    while True:
        player_response = input("Would you like to hit or stand? Either type 'h' or 's'.\n: ")

        if player_response[0].lower() == 'h':
            player.add_card(deck.deal())

        elif player_response[0] == 's':
            print("Player choose to stand. Dealer's turn.")
            break

        else:
            print("Sorry that was not a valid input please select 'hit' or 'stand'.")
            continue
        break