"""
Connor Mentel 
morse_part2
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


# Asking user their intention
def choice():
    pick = input(
        "Would you like to:\nA.Convert from Morse to English\nB.Convert from English to Morse?\nC.Quit\n").upper()
    if pick == ("A"):
        ME()
    elif pick == ("B"):
        EM()
    elif pick == ("C"):
        exit()
    else:
        print("Please select from above.")
        choice()


# Converting English to Morse
def convert1(latin):
    for x in LIST:
        if x[0] == latin:
            return x[1]
    return ''


# Converting Morse to English
def convert2(morse):
    for x in LIST:
        if x[1] == morse:
            return x[0]
    return ''


# English to Morse Function
def EM():
    message = ""
    while message != ":q:":
        message = input("\nWhat's your sentence?\nEnter :q: when finished!\n")
        print("You entered,", message)
        message2 = message.upper()
        bank = []
        if message != ":q:":
            for i in message2:
                bank.append(convert1(i))
            print("The Morse code translation is", ' '.join(bank))
        else:
            print("Thanks for using Morse Translator! Have a good day!")
            break


# Morse to English Function
def ME():
    message = ""
    while message != ([':q:']):
        message = input("\nWhat's your sentence?\nEnter :q: when finished!\n").split()
        print("You entered,", message)
        message2 = message
        bank = []
        if message != ([':q:']):
            for i in message2:
                bank.append(convert2(i))
            print("The English translation is", ' '.join(bank))
        else:
            print("Thanks for using Morse Translator! Have a good day!")
            break


# Main Function
# I had to create more functions duplicating the calls but reversing them.
def main():
    choice()


main()
