'''
Connor Mentel
Casino
Last Mod: 8/4/20
'''

from Casino import poker
from Casino import roulette
from Casino import blackjack


class Casino:
    def __init__(self):
        self.bank = 200

    # playing poker
    def play_poker(self):
        pokering = True
        while pokering:
            pokergame = poker.Poker(self.bank)
            pokergame.options()
            if pokergame.bank <= 0:
                pokering = False
                print("You're broke!\n")
                self.bank = pokergame.bank
                return
            self.bank = pokergame.bank
            print("Would you like to play poker again? ('Yes' or 'No') Your bank is:", self.bank, "\n")
            poker_decision = input().lower()
            if poker_decision == "yes" or poker_decision == "y":
                continue
            else:
                pokering = False
                print("Thanks for playing poker!\n")
                self.bank = pokergame.bank
                break

    # playing blackjack
    def play_blackjack(self):
        blackjacking = True
        while blackjacking:
            bjgame = blackjack.Blackjack(self.bank)
            bjgame.options()
            if bjgame.bank <= 0:
                blackjacking = False
                print("You're broke!\n")
                self.bank = bjgame.bank
                return
            self.bank = bjgame.bank
            print("Would you like to play blackjack again? ('Yes' or 'No') Your bank is:", self.bank, "\n")
            blackjack_decision = input().lower()
            if blackjack_decision == "yes" or blackjack_decision == "y":
                continue
            else:
                blackjacking = False
                print("Thanks for playing Blackjack!\n")
                self.bank = bjgame.bank
                break

    # playing roulette
    def play_roulette(self):
        rouletting = True
        while rouletting:
            roulettegame = roulette.Roulette(self.bank)
            roulettegame.options()
            if roulettegame.bank <= 0:
                rouletting = False
                print("You're broke!\n")
                self.bank = roulettegame.bank
                return
            self.bank = roulettegame.bank
            print("Would you like to play roulette again? ('Yes' or 'No') Your bank is:", self.bank, "\n")
            roulette_decision = input().lower()
            if roulette_decision == "yes" or roulette_decision == "y":
                continue
            else:
                rouletting = False
                print("Thanks for playing poker!\n")
                self.bank = roulettegame.bank
                break

    # method to choose game / table.
    def go_to_table(self):
        print("Welcome to Connor's casino!!\nWe've given you $200 in chips to start\n")
        gambling = True
        while gambling:
            # if broke
            if self.bank == 0:
                gambling = False
                return

            game_choice = str(
                input("What game would you like to play?\nA. Poker\nB. Black Jack\nC. Roulette\nD. Quit\n").lower())

            # Playing Poker
            if game_choice == "a":
                self.play_poker()

            # Playing Blackjack
            elif game_choice == "b":
                self.play_blackjack()

            # Playing Roulette
            elif game_choice == "c":
                self.play_roulette()

            # Exiting
            elif game_choice == "d":
                gambling = False
                break

            else:
                print("Please select from the above!")
                continue
