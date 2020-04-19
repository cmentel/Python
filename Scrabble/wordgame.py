'''
Connor Mentel
CS 5001
HW 6
Programming 2
wordgame.py
'''

# imports
from Scrabble.scrabble_points import *
from Scrabble.wordlist import *
import random


# assigns temporary variable to function call
from Scrabble.wordlist import get_wordlist

tmp = get_wordlist()


# appends the words from the get_wordlist function to an empty list
wordlist = []
for word in tmp:
    word = word.rstrip()
    wordlist.append(word)


# dictionaries of letter frequency
letter_frequency_dict = {'J': 1, 'K': 1, 'Q': 1, 'X': 1, 'Z': 1, 'B': 2, 'C': 2, 'F': 2,
                         'H': 2, 'M': 2, 'P': 2, 'V': 2, 'W': 2, 'Y': 2, 'blank': 2, 'G': 3,
                         'D': 4, 'L': 4, 'S': 4, 'U': 4, 'N': 6, 'R': 6, 'T': 6, 'O': 8, 'A': 9,
                         'I': 9, 'E': 12}


# dictionaries of letter values
letter_points_dict = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1,
                      'R': 1, 'D': 2, 'G': 2,'B': 3, 'C': 3, 'M': 3, 'P': 3,'F': 3, 'H': 3, 'V': 3,
                      'W': 3, 'Y': 3,'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}


'''
    Function that plays the game and prompts user for input and runs a lop with nested
    if statements to enter commands for the game.
    Parameters: Nothing
    Returns: Nothing
    Does: Plays the game created on a loop based on user input
    will be appended to dictionary and run through class.
'''

def main():
    words = []
    total_points = 0
    playing = True
    while playing == True:

        user_input = input("Please select from one of the follow options: \n"
                           "D : Draw 7 letters from the bag \n"
                           "W : Make a word from the letters in play \n"
                           "P : Print all words played so far \n"
                           "Q : Quit \n")

        # If user input is D, draw letters from the bag
        if user_input == "D" or user_input == "d":

            # empty list of the letters drawn
            result = []

            # for loop to select seven letters from the dictionary
            for i in range(7):

                # attempt to grab letters
                try:
                    c = random.choice(bag_of_letters(letter_frequency_dict))

                # exception for if seven letters cannot be drawn
                except IndexError:
                    print("Bag is empty!")
                    playing = False

                # otherwise appends the letter to the result list
                else:
                    result.append(c)

                    # iterates through the list of letters drawn
                    for r in result:

                        # if the letter appears in the dictionary
                        if r in letter_frequency_dict.keys():

                            # deletes the letter
                            del letter_frequency_dict[r]

            print(result)


        # If user input is to make a word from the letters in play
        elif user_input == "W" or user_input == "w":

            # takes input and validates that all letters are part of drawing
            go = True
            while go == True:
                user_word = input("Enter word:\n")
                user_word = user_word.upper()


                hit = 0
                for letter in user_word:
                    if letter not in result:
                        hit = 1
                        print("Incorrect letter used. Try again.")
                if hit == 0:
                    go = False

            # if input is valid
            if user_word in wordlist:

                # calculates the point values of each letter and adds to be total for that word
                points = get_word_value(user_word, letter_points_dict)

                # adds total points with points of word played
                total_points = total_points + points
                print("You have",total_points,"points total!")

                #appends the word played to existing word list
                words.append(user_word)

                #removes the letters in the word from the bag
                for letter in user_word:
                    result.remove(letter)


                # gets the number of replacement letters to be played
                n_replacements = 7 - len(result)

                # if statement to try to get more letters, raises error if not enough letters in bag
                if n_replacements > 0:
                    for i in range(n_replacements):
                        try:
                            c = random.choice(bag_of_letters(letter_frequency_dict))
                        except IndexError:
                            print("Bag is empty!")
                            playing = False
                        else:
                            result.append(c)
                    print("Here are your new letters: ", result)

            else:


                used = 0
                for word in wordlist:
                    for letter in user_word:
                        if letter not in user_word:
                            used = used + 1
                    if used == 1:
                        # blank tile used!

                        # calls function get_word_value
                        points = get_word_value(user_word, letter_points_dict)

                        # adds to points from function
                        total_points = total_points + points

                        # prints the point value
                        print("You have ", total_points, " points total!\n")

                        # appends word to the words
                        words.append(user_word)

                        # removes letters from bag
                        for letter in user_word:
                            result.remove(letter)
                        n_replacements = 7 - len(result)

                        # checks to see if new letters can be drawn
                        if n_replacements > 0:
                            for i in range(0, n_replacements - 1):
                                try:
                                    c = random.choice(bag_of_letters(letter_frequency_dict))
                                except IndexError:
                                    print("Bag is empty!")
                                    playing = False
                                else:
                                    result.append(c)
                                    print("Here are your new letters: ", result)

        # prints the words played
        elif user_input == "P" or user_input == "p":
            print(words)

        # quits the game
        elif user_input == 'Q' or user_input == 'q':
            print("Thanks for playing!")
            playing = False

        # validates input
        else:
            print("Unacceptable input.")


main()