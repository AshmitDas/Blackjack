def Game_scenario():

    def dealer_Wins(chips):
    
        print("Dealers Win!")
        chips.bet_lost()


    def dealer_busts(chips):

        print("Dealer busts!")
        chips.bet_won()

    
    def player_win(chips):

        print("Player wins!")
        chips.bet_won()


    def player_busts(chips):

        print("Players busts.")
        chips.bet_lost()