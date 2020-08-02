'''
Connor Mentel
Casino
Last Mod: 8/2/20
'''

from Casino import poker
from Casino import roulette


class Casino:
    def __init__(self):
        self.bank = 200
        self.go_to_table()

    # method to play poker.
    def play_poker(self):
        pokering = True
        while pokering:
            game = poker.Poker(self.bank)
            game.options()
            print("Would you like to play poker again? ('Yes' or 'No') Your bank is:", game.bank, "\n")
            poker_decision = input().lower()
            if poker_decision == "yes" or poker_decision == "y":
                continue
            else:
                pokering = False
                print("Thanks for playing poker!\n")
                self.bank = game.bank
                break

    # method to play roulette.
    def play_roulette(self):
        rouletting = True
        while rouletting:
            game = roulette.Roulette(self.bank)
            game.options()
            print("Would you like to play poker again? ('Yes' or 'No') Your bank is:", game.bank, "\n")
            roulette_decision = input().lower()
            if roulette_decision == "yes" or roulette_decision == "y":
                continue
            else:
                rouletting = False
                print("Thanks for playing poker!\n")
                self.bank = game.bank
                break

    # method to choose game / table.
    def go_to_table(self):
        print("Welcome to Connor's casino!!\nWe've given you $200 in chips to start\n\n")
        gambling = True
        while gambling:
            game_choice = str(
                input("What game would you like to play?\nA. Poker\nB. Black Jack\nC. Roulette\nD. Quit\n").lower())
            if game_choice == "a":
                self.play_poker()

            # TODO implement blackjack
            elif game_choice == "b":
                pass

            elif game_choice == "c":
                self.play_roulette()

            elif game_choice == "d":
                gambling = False
                break

            else:
                print("Please select from the above!")
                continue
