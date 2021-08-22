def take_bet(chips):
    
    while True :
        try : 

            chips.bet = int(input("Amount you want to bet : "))

        except:

            print("Kindly enter integer value to continue.")

        else :
            if chips.bet > chips.total :
                print(f'You have entered entered bet amout which is greater than your total : {chips.total}.\nPlease Kindly enter within the total value range.')

            else:
                break