"""
Connor Mentel 
morse_part1
CS 5001
HW3
"""

LIST = [[' ', '/'], ['A', '.-'], ['B', '-...'], ['C', '-.-.'], ['D', '-..'], ['E', '.'],
        ['F', '..-.'], ['G', '--.'], ['H', '....'], ['I', '..'], ['J', '.---'],
        ['K', '-.-'], ['L', '.-..'], ['M', '--'], ['N', '-.'], ['O', '---'],
        ['P', '.--.'], ['Q', '--.-'], ['R', '.-.'], ['S', '...'], ['T', '-'],
        ['U', '..-'], ['V', '...-'], ['W', '.--'], ['X', '-..-'], ['Y', '-.--'], ['Z', '--..'], ['0', '-----'],
        ['1', '.----'], ['2', '..---'], ['3', '...--'], ['4', '....-'], ['5', '.....'], ['6', '-....'], ['7', '--...'],
        ['8', '---..'], ['9', '----.'], ['?', '..--..'], ['!', '-.-.--'], ['\'', '.----.'], ['"', '.-..-.'],
        [',', '--..--']]


# Converting English to Morse
def convert(latin):
    for x in LIST:
        if x[0] == latin:
            return x[1]
    return ''


# Takes message and converts to Morse and prints
def main():
    message = ""
    while message != ":q:":
        message = input("\nWhat's your sentence?\nEnter :q: when finished!\n")
        print("You entered,", message)
        message2 = message.upper()
        bank = []
        if message != ":q:":
            for i in message2:
                bank.append(convert(i))
            print("The Morse code translation is", ' '.join(bank))

        else:
            print("Thanks for using Morse Translator! Have a good day!")
            break


main()
