'''
Connor Mentel
Word Manipulation
Last Mod 5/10/2020
'''


def backwards(word):
    print("Here is the word spelled backwards:", word[::-1], "\n")
    option(word)


def count(word):
    vowel_counter = 0
    consonants_counter = 0
    letter_counter = 0
    word_capital = word.upper()
    for i in word_capital:
        word_capital = word.upper()
        letter_counter = letter_counter + 1
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            vowel_counter = vowel_counter + 1

    consonants_counter = letter_counter - vowel_counter

    print("In", word, "there are", letter_counter, "letters,", vowel_counter, "vowels, and", consonants_counter,
          "consonants.\n")
    option(word)


def palindrome(word):
    word_capital = word.upper()
    if word_capital[::-1] == word_capital:
        print(word, "is a palindrome :)\n")
    else:
        print(word, "is not a palindrome :(\n")

    option(word)


def main():
    word = input("Hi! Please enter a word.\n")
    # If word contains a number or there is a space in the word start over.
    if ' ' in word or any(char.isdigit() for char in word):
        print("Please enter a word!\n")
        main()

    option(word)


def option(word):
    option = str(input("What would you like to do with this word? Please enter the number of the option:\n"
                       "1. Spell it backwards\n"
                       "2. Count the vowels, consonants, and letters\n"
                       "3. Check if its a palindrome\n"
                       "4. Exit\n"))
    if option == '1':
        backwards(word)
    elif option == '2':
        count(word)
    elif option == '3':
        palindrome(word)
    elif option == '4':
        exit("I hope you have a good day!\n")
    else:
        print("Please enter the number of the option you'd like to use!\n")
        main()


main()
