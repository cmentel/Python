'''
Connor Mentel
Casino
Last Mod: 8/1/20
'''

from Casino import poker
from Casino import roulette

class Casino:
    def __init__(self):
        self.bank = 200
        self.go_to_table()

    def play_poker(self):
        pokering = True
        while pokering:
            game = poker.Poker(self.bank)
            game.options()
            print("Would you like to play poker again? ('Yes' or 'No') Your bank is:",game.bank,"\n")
            poker_decision = input().lower()
            if poker_decision == "yes" or poker_decision == "y":
                continue
            else:
                pokering = False
                print("Thanks for playing poker!\n")
                self.bank = game.bank
                break


    def play_roulette(self):
        roulette.initialize(self.bank)

    def go_to_table(self):
        print("Welcome to Connor's casino!!\nWe've given you $200 in chips to start\n\n")
        gambling = True
        while gambling:
            game_choice = str(input(
                "What game would you like to play?\nA. Poker\nB. Black Jack\nC. Roulette\nD. Quit\n").lower())
            if game_choice == "a":
                self.play_poker()
            elif game_choice == "c":
                self.play_roulette()
            elif game_choice == "d":
                gambling = False
                break
            else:
                print("Please select from the above!")
                continue
