'''
Connor Mentel
Casino
Last Mod: 8/1/20
'''

from Casino import poker
from Casino import roulette


def play_poker(bank):
    return poker.initialize(bank)


def play_roulette(bank):
    return roulette.initialize(bank)


def initialize_casino(BANK):
    gambling = True
    while gambling:
        game_choice = input(
            "What game would you like to play?\nA. Poker\nB. Black Jack\nC. Roulette\nD. Quit\n").lower()
        if game_choice == "c":
            play_roulette(BANK)
        elif game_choice == "a":
            play_poker(BANK)
        elif game_choice == "d":
            gambling = False
            break
        else:
            print("Please select from the above!")
            continue


initialize_casino(200)
