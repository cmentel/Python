'''
Rock Paper Scissors
Last mod: 7/18/20
'''


def initialize():
    games = 0
    player_one_wins = 0
    player_two_wins = 0
    player_one = input("Who is player one?\n")
    player_two = input("Who is player two?\n")
    games_to_play = int(input("How many games would you like to play?\n"))
    play_game(games, player_one, player_two, player_one_wins, player_two_wins, games_to_play)


def play_game(games, player_one, player_two, player_one_wins, player_two_wins, games_to_play):
    # loop to play game
    games += 1
    while games <= games_to_play:
        print("GAME:", games)
        print(player_one, "what's your hand?")
        player_one_guess = input().upper()
        print(player_two, "what's your guess?")
        player_two_guess = input().upper()

        # logic handing outcome of players
        if player_one_guess == 'ROCK':
            if player_two_guess == 'SCISSORS':
                print(player_one, "wins that round\n")
                player_one_wins += 1
            elif player_two_guess == 'ROCK':
                print("It's a tie!\n")
            elif player_two_guess == "PAPER":
                print(player_two, "wins that round!\n")
                player_two_wins += 1
            else:
                print("Please enter either 'Rock', 'Paper', or 'Scissors'\n")
                continue

        elif player_one_guess == 'PAPER':
            if player_two_guess == 'SCISSORS':
                print(player_two, "wins that round\n")
                player_two_wins += 1
            elif player_two_guess == 'PAPER':
                print("It's a tie!\n")
            elif player_two_guess == "ROCK":
                print(player_one, "wins that round!\n")
                player_one_wins += 1
            else:
                print("Please enter either 'Rock', 'Paper', or 'Scissors'\n")
                continue

        elif player_one_guess == 'SCISSORS':
            if player_two_guess == 'ROCK':
                print(player_two, "wins that round\n")
                player_two_wins += 1
            elif player_two_guess == 'SCISSORS':
                print("It's a tie!\n")
            elif player_two_guess == "PAPER":
                print(player_one, "wins that round!\n")
                player_one_wins += 1
            else:
                print("Please enter either 'Rock', 'Paper', or 'Scissors'\n")
                continue

        else:
            print("Please enter either 'Rock', 'Paper', or 'Scissors'\n")
            continue

        # increment number of games played
        games += 1

        # prints games played and current score
        print(print_score(player_one, player_two, player_one_wins, player_two_wins))

    # prints name of winner or if there was a tie
    get_winner(player_one, player_two, player_one_wins, player_two_wins)

    # asks to play again ?
    if play_again(games_to_play) == True:
        initialize()
    else:
        exit("Thanks for playing!\n")


def get_winner(player_one, player_two, player_one_wins, player_two_wins):
    if player_one_wins > player_two_wins:
        print(player_one, "wins!\n", print_score(player_one, player_two, player_one_wins, player_two_wins))
    elif player_two_wins > player_one_wins:
        print(player_two, "wins!\n", print_score(player_one, player_two, player_one_wins, player_two_wins))
    else:
        print("It's a tie!!\nGood game", player_one, "and", player_two, "\n")


def print_score(player_one, player_two, player_one_wins, player_two_wins):
    score_string = "SCORE:\n"
    player_one_string = player_one + " has " + str(player_one_wins)
    player_two_string = player_two + " has " + str(player_two_wins)

    if player_one_wins == 1 and player_two_wins == 1:
        return score_string + player_one_string + " win \n" + player_two_string + " win\n"

    elif player_one_wins == 1 and player_two_wins != 1:
        return score_string + player_one_string + " win \n" + player_two_string + " wins\n"

    elif player_one_wins != 1 and player_two_wins == 1:
        return score_string + player_one_string + " wins \n" + player_two_string + " win\n"
    else:
        return score_string + player_one_string + " wins \n" + player_two_string + " wins\n"


def play_again(games_to_play):
    print("That's",games_to_play,"games!")
    option = input("Would you want to play again?\n")
    if option.upper() == "YES":
        return True
    elif option.upper() == "NO":
        return False
    else:
        play_again(games_to_play)


initialize()
