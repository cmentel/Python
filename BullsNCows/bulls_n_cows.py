'''
Connor Mentel
CS 5001 - HW 5
Programming #2
Due: Thursday October 31
'''

# imports
import random

# selects four random integers from, 0 to 9, to be the 'secret_code' (w/out duplicates)
secret_code = random.sample(range(10), 4)


# funtion to keep a running ledger of attempts
def historyy(g_list, history):
    history = history + [g_list]
    for i in history:
        print("Here is your guess history", i, )
    return history


# function to count and assign the cows and bulls
def count_bulls_and_cows(g_list):
    bulls = 0
    cows = 0

    # for loop that iterates through all elements of the guess and compares with the secret_code.
    for i in range(len(g_list)):

        # if the element matches value and position
        if g_list[i] == secret_code[i]:
            bulls = bulls + 1

        # if the element does not match the value and position AND the element is in the secret_code.
        elif g_list[i] != secret_code[i] and g_list[i] in secret_code:
            cows = cows + 1

        elif bulls == 4:
            return bulls, cows
    print("Bulls:", bulls, "Cows:", cows)
    return [cows, bulls]


# main function that tests input, runs program, and prints if user wins or loses
def main():
    # bank of attempts HELP
    tries = 0

    # bank of the guesses:
    history = []

    # while tries is less than or equal to 7
    while tries <= 7:

        print("\nTries:", tries)

        # asks user for guess
        guess = input("Enter your guess. Numbers separated by a space.\n")

        # converts input to list
        g_list = list(map(int, guess.split()))

        # checks that no integer is greater than or equal to 10
        for i in g_list:
            if i >= 10:
                print("Please enter four different numbers from 0-9")
                continue
            else:
                continue

        # checks to see if the input is 4 different numbers
        if (len(set(g_list)) <= 3) or 0 == sum(g_list):
            print("Please enter four different numbers from 0 - 9")
            continue

        # if user guesses the correct secret_code
        elif g_list == secret_code:
            print("Congratulations you guessed", secret_code, "correctly!")
            break

        # passed all barriers and now will run the function
        else:
            count_bulls_and_cows(g_list)
            # runs function to ledger
            history = historyy(g_list, history)

        tries += 1
        continue

    # alerting player that they didn't guess correctly
    if tries == 8:
        print("\nSorry you didn't manage to guess in time! :(\nthe answer is:", secret_code)

        # asks if user wants to play again
        again = input("Play again? 'Y' or 'N'\n")
        if again == "Y":
            main()
        else:
            exit()


main()
