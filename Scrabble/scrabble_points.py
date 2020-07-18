'''
Connor Mentel
CS 5001
HW 6
Programming 2
scrabble_points.py
'''


def bag_of_letters(letter_frequency_dict):
    letters = []

    for key in letter_frequency_dict:
        tmp = key * letter_frequency_dict[key]

        if key != "blank":
            tmp = list(tmp)

            for i in tmp:
                letters.append(i)

    return letters


def get_word_value(word, letter_points_dict):
    word = word.upper()
    word = list(word)

    total_points = 0

    for letter in word:
        points = letter_points_dict[letter]
        total_points = total_points + points

    return total_points
