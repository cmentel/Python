'''
Rock Paper Scissors
Last mod: 7/21/20
'''

import random

options = ["ROCK", "PAPER", "SCISSORS"]

player_one = input("What is your name?\n")


def initialize():
    games = 0
    player_one_wins = 0
    computer_wins = 0
    computer = "Computer"
    games_to_play = int(input("How many games would you like to play?\n"))
    play_game(games, player_one, computer, player_one_wins, computer_wins, games_to_play)


def play_game(games, player_one, computer, player_one_wins, computer_wins, games_to_play):
    # loop to play game
    games += 1
    while games <= games_to_play:
        print("GAME:", games)
        print(player_one, "what's your hand?")
        player_one_guess = input().strip().upper()
        computer_guess = random.choice(options)
        print("Computer's hand:", computer_guess)

        # logic handing outcome of players
        if player_one_guess == 'ROCK':
            if computer_guess == 'SCISSORS':
                print(player_one, "wins that round\n")
                player_one_wins += 1
            elif computer_guess == 'ROCK':
                print("It's a tie!\n")
            elif computer_guess == "PAPER":
                print(computer, "wins that round!\n")
                computer_wins += 1
            else:
                print("Please enter either 'Rock', 'Paper', or 'Scissors'\n")
                continue

        elif player_one_guess == 'PAPER':
            if computer_guess == 'SCISSORS':
                print(computer, "wins that round\n")
                computer_wins += 1
            elif computer_guess == 'PAPER':
                print("It's a tie!\n")
            elif computer_guess == "ROCK":
                print(player_one, "wins that round!\n")
                player_one_wins += 1
            else:
                print("Please enter either 'Rock', 'Paper', or 'Scissors'\n")
                continue

        elif player_one_guess == 'SCISSORS':
            if computer_guess == 'ROCK':
                print(computer, "wins that round\n")
                computer_wins += 1
            elif computer_guess == 'SCISSORS':
                print("It's a tie!\n")
            elif computer_guess == "PAPER":
                print(player_one, "wins that round!\n")
                player_one_wins += 1
            else:
                print("Please enter either 'Rock', 'Paper', or 'Scissors'\n")
                continue

        else:
            print("Please enter either 'Rock', 'Paper', or 'Scissors'\n")
            continue

        # prints games played and current score
        print(print_score(player_one, computer, player_one_wins, computer_wins))

        # if outcome is immutable, break loop
        if computer_wins > games_to_play / 2 or player_one_wins > games_to_play / 2:
            break

        # increment number of games played
        games += 1

    # prints name of winner or if there was a tie
    get_winner(player_one, computer, player_one_wins, computer_wins)

    # asks to play again ?
    if play_again(games - 1) == True:
        initialize()
    else:
        exit("Thanks for playing!\n")


def get_winner(player_one, computer, player_one_wins, computer_wins):
    if player_one_wins > computer_wins:
        print(player_one, "wins!\n\n", print_score(player_one, computer, player_one_wins, computer_wins))
    elif computer_wins > player_one_wins:
        print(computer, "wins!\n\n", print_score(player_one, computer, player_one_wins, computer_wins))
    else:
        print("It's a tie!!\nGood game", player_one, "and", computer, "\n")


def print_score(player_one, computer, player_one_wins, computer_wins):
    player_one_string = player_one + " has " + str(player_one_wins)
    computer_string = computer + " has " + str(computer_wins)

    if player_one_wins == 1 and computer_wins == 1:
        return "SCORE:\n" + player_one_string + " win \n" + computer_string + " win\n"

    elif player_one_wins == 1 and computer_wins != 1:
        return "SCORE:\n" + player_one_string + " win \n" + computer_string + " wins\n"

    elif player_one_wins != 1 and computer_wins == 1:
        return "SCORE:\n" + player_one_string + " wins \n" + computer_string + " win\n"
    else:
        return "SCORE:\n" + player_one_string + " wins \n" + computer_string + " wins\n"


def play_again(games):
    if games == 1:
        print("That's", games, "game!")
    else:
        print("That's", games, "games!")
    option = input("Would you want to play again? ('YES' or 'NO')\n")
    if option.upper() == "YES":
        return True
    elif option.upper() == "NO":
        return False
    else:
        play_again(games)


initialize()
