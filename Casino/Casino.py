'''
Connor Mentel
Scratch File_6
Last Mod:
Jan 2 2020
'''

import random

print("Hello and welcome to Connor's Casino!\nWhat game would you like to play?\nA. Poker\nB. Black Jack\nC. Roulette\nD. Quit")

def poker():
    POKER_BANK = 200
    CARDS = {"Ace":4,"2":4,"3":4,"4":4,"5":4,"6":4,"7":4,"8":4,"9":4,"10":4,"Jack":4,"Queen":4,"King":4}
    SUITS = {"Hearts":13,"Spades":13,"Clubs":13,"Diamonds":13}

    # Creates a dictioary from the keys of SUITS
    SUITS_KEYS = dict.fromkeys(SUITS)

    SUITS_HAND = random.sample(list(SUITS_KEYS),5)

    # Creates a dicionary from the keys of CARDS
    CARDS_KEYS = dict.fromkeys(CARDS)

    CARD_KEYS_HAND = random.sample(list(CARDS_KEYS),5)
    print("\nHere is suits for hand:",SUITS_HAND,"\nHere is cards for hand:",CARD_KEYS_HAND)


    #POKER_HAND = random.sample(POKER_CARD_DICT,5)
    #print(POKER_HAND)

    #cards = random.sample(POKER_CARDS,5)
    #suits = random.sample(POKER_SUITS,5)


    #print(suits,cards)


def roulette():
    ROULETTE_BANK = 100
    ROULETTE_COLORS = ["Black", "Red"]
    ROULETTE_TVALUES = ["Odd", "Even"]
    ROULETTE_VALUES = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    ROULETTE_RED_NUMS = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    ROULETTE_BLACK_NUMS = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

    playing = True

    while playing == True:
        shift = input("Would you like to wager the:\nA. Color\nB. Odd or Even\nC. High or Low\nD. Color and Number\nE. Quit\n\n")

        if shift == "A" or shift == "a":
            r_bet = int(input("How much would you like to wager?\n"))
            ROULETTE_BANK = ROULETTE_BANK - r_bet
            r_color = input("What color would you like to bet? 'Red' or 'Black' ?\n")
            r_color = r_color.capitalize()
            print("Rolling Rolling Rolling...")
            a_color = random.choice(ROULETTE_COLORS)
            a_color = a_color.capitalize()
            print("The rolled color is:",a_color)
            if a_color == r_color:
                print("Congrats you won!")
                ROULETTE_BANK = ROULETTE_BANK + (r_bet * 2)
                print("Your current bank is:", ROULETTE_BANK)

            else:
                print("You didn't win this time! Try again!")
                print("Your current bank is:", ROULETTE_BANK)

        elif shift == "E" or shift == "e":
            print("Thank you for playing! Your total winnings are: $",ROULETTE_BANK)
            pa = input("Would you like to return to the casino floor?")
            if pa == "Yes" or pa == "yes":
                casino()
            else:
                print("Thank you for playing!!")
                break

        elif shift == "B" or shift == "b":
            r_bet = int(input("How much would you like to wager?\n"))
            ROULETTE_BANK = ROULETTE_BANK - r_bet
            r_value = input("Do you guess 'Odd' or 'Even' ?\n")
            r_value = r_value.capitalize()
            print("Rolling Rolling Rolling...")
            e_value = random.choice(ROULETTE_TVALUES)
            e_value = e_value.capitalize()
            print("The rolled value is:", e_value)
            if e_value == r_value:
                print("Congrats you won!")
                ROULETTE_BANK = ROULETTE_BANK + (r_bet + r_bet)
                print("Your current bank is:", ROULETTE_BANK)
            else:
                print("You didn't win this time! Try again!")
                print("Your current bank is:", ROULETTE_BANK)

        elif shift == "C" or shift == "c":
            r_bet = int(input("How much would you like to wager?\n"))
            ROULETTE_BANK = ROULETTE_BANK - r_bet
            r_value = input("Do you guess 'High' or 'Low'?\n")
            r_value = r_value.capitalize()
            print("Rolling Rolling Rolling...")
            c_value = random.choice(ROULETTE_VALUES)
            print("The rolled number is:", c_value)
            if r_value == "High" or r_value == "high":
                if c_value > 18:
                    print("Congrats you won!")
                    ROULETTE_BANK = ROULETTE_BANK + (r_bet * 2)
                    print("Your current bank is:", ROULETTE_BANK,"\n")
                else:
                    print("You didn't win this time! Try again!")
                    print("Your current bank is:", ROULETTE_BANK,"\n")
            elif r_value == "Low" or r_value == "low":
                if c_value <= 18:
                    print("Congrats you won!")
                    ROULETTE_BANK = ROULETTE_BANK + (r_bet * 2)
                    print("Your current bank is:", ROULETTE_BANK,"\n")
                else:
                    print("You didn't win this time! Try again!")
                    print("Your current bank is:", ROULETTE_BANK,"\n")

        elif shift == "D" or shift == "d":
            r_bet = int(input("How much would you like to wager?\n"))
            ROULETTE_BANK = ROULETTE_BANK - r_bet
            play = True
            while play == True:
                r_color = input("What color would you like to bet? 'Red' or 'Black' ?\n")
                if r_color == "Red" or r_color == "red":
                    r_value = int(input("What number do you guess?\n"))
                    if r_value not in ROULETTE_RED_NUMS:
                        print("That number is not red. Please select again.\n")
                    else:
                        print("Rolling Rolling Rolling...\n")
                        d_color = random.choice(ROULETTE_RED_NUMS)
                        if d_color == r_value:
                            print("The number rolled was a Red",d_color,"\n")
                            print("Congrats you won!")
                            ROULETTE_BANK = ROULETTE_BANK + (r_bet * 4)
                            print("Your current bank is:", ROULETTE_BANK,"\n")
                            break
                        else:
                            print("The number rolled was a Red", d_color, "\n")
                            print("You didn't win this time! Try again!\n")
                            print("Your current bank is:", ROULETTE_BANK,"\n")
                            break

                if r_color == "Black" or r_color == "black":
                    r_value = int(input("What number do you guess?\n"))
                    if r_value not in ROULETTE_BLACK_NUMS:
                        print("That number is not black. Please select again.\n")
                    else:
                        print("Rolling Rolling Rolling...\n")
                        d_color = random.choice(ROULETTE_RED_NUMS)
                        if d_color == r_value:
                            print("The number rolled was a Black", d_color, "\n")
                            print("Congrats you won!")
                            ROULETTE_BANK = ROULETTE_BANK + (r_bet * 4)
                            print("Your current bank is:", ROULETTE_BANK,"\n")
                            break

                        else:
                            print("The number rolled was a Red", d_color, "\n")
                            print("You didn't win this time! Try again!\n")
                            print("Your current bank is:", ROULETTE_BANK,"\n")
                            break

        else:
            print("Please select from the above.\n")

        if ROULETTE_BANK <= 0:
            print("Sorry you're broke! Have a great night!")
            return

def casino():

    x = input("What game do you want to play?\n")
    if x == "C" or x == "c":
        print("Welcome to the Roulette Table! We've given you $100 in chips to start!\n")
        roulette()
    elif x == "A" or x == "a":
        print("Welcome to the Poker Table! We've given you $200 in chips to start!\n")
        poker()
    else:
        print("Please select from the above!")
        casino()
casino()