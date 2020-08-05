'''
Connor Mentel
Roulette
Last mod: 8/4/20
'''

import random

ROULETTE_COLORS = ["BLACK", "RED"]
ROULETTE_TVALUES = ["ODD", "EVEN"]
ROULETTE_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
ROULETTE_RED_NUMS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
ROULETTE_BLACK_NUMS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


class Roulette:
    def __init__(self, bank):
        self.bank = bank

    # wager color
    def wager_color(self):
        print("How much would you like to wager?\nYour bank is:", self.bank)
        r_bet = int(input())
        self.bank = self.bank - r_bet
        r_color = input("What color would you like to bet? 'Red' or 'Black' ?\n").upper()
        a_color = random.choice(ROULETTE_COLORS)
        print("The rolled color is:", a_color)
        if a_color == r_color:
            print("Congrats you won!")
            self.bank = self.bank + (r_bet * 2)
            print("Your current bank is:", self.bank)

        else:
            print("You didn't win this time! Try again!")
            print("Your current bank is:", self.bank)

    # wager odd or even
    def wager_odd_or_even(self):
        print("How much would you like to wager?\nYour bank is:", self.bank)
        r_bet = int(input())
        self.bank = self.bank - r_bet
        r_value = input("Do you guess 'Odd' or 'Even' ?\n").upper()
        e_value = random.choice(ROULETTE_TVALUES)
        print("The rolled value is:", e_value)
        if e_value == r_value:
            print("Congrats you won!")
            self.bank = self.bank + (r_bet * 2)
            print("Your current bank is:", self.bank)
        else:
            print("You didn't win this time! Try again!")
            print("Your current bank is:", self.bank)

    # wager high or low
    def high_or_low(self):
        print("How much would you like to wager?\nYour bank is:", self.bank)
        r_bet = int(input())
        self.bank = self.bank - r_bet
        r_value = input("Do you guess 'High' or 'Low'?\n").upper()
        c_value = random.choice(ROULETTE_VALUES)
        print("The rolled number is:", c_value)
        if r_value == "HIGH":
            if c_value > 18:
                print("Congrats you won!")
                self.bank = self.bank + (r_bet * 3)
                print("Your current bank is:", self.bank, "\n")
            else:
                print("You didn't win this time! Try again!")
                print("Your current bank is:", self.bank, "\n")
        elif r_value == "LOW":
            if c_value <= 18:
                print("Congrats you won!")
                self.bank = self.bank + (r_bet * 3)
                print("Your current bank is:", self.bank, "\n")
            else:
                print("You didn't win this time! Try again!")
                print("Your current bank is:", self.bank, "\n")

    # wager color and number
    def color_and_number(self):
        print("How much would you like to wager?\nYour bank is:", self.bank)
        r_bet = int(input())
        self.bank = self.bank - r_bet
        play = True
        while play == True:
            r_color = input("What color would you like to bet? 'Red' or 'Black' ?\n").upper()
            if r_color == "RED":
                r_value = int(input("What number do you guess?\n"))
                if r_value not in ROULETTE_RED_NUMS:
                    print("That number is not red. Please select again.\n")
                else:
                    d_color = random.choice(ROULETTE_RED_NUMS)
                    if d_color == r_value:
                        print("The number rolled was a Red", d_color, "\n")
                        print("Congrats you won!")
                        self.bank = self.bank + (r_bet * 4)
                        print("Your current bank is:", self.bank, "\n")
                        break
                    else:
                        print("The number rolled was a Red", d_color, "\n")
                        print("You didn't win this time! Try again!\n")
                        print("Your current bank is:", self.bank, "\n")
                        break

            if r_color == "BLACK":
                r_value = int(input("What number do you guess?\n"))
                if r_value not in ROULETTE_BLACK_NUMS:
                    print("That number is not black. Please select again.\n")
                else:
                    d_color = random.choice(ROULETTE_BLACK_NUMS)
                    if d_color == r_value:
                        print("The number rolled was a Black", d_color, "\n")
                        print("Congrats you won!")
                        self.bank = self.bank + (r_bet * 4)
                        print("Your current bank is:", self.bank, "\n")
                        break

                    else:
                        print("The number rolled was a Red", d_color, "\n")
                        print("You didn't win this time! Try again!\n")
                        print("Your current bank is:", self.bank, "\n")
                        break

    # options to play game
    def options(self):
        playing = True
        while playing == True:

            # if broke
            if self.bank <= 0:
                playing = False
                break

            shift = str(input(
                "Would you like to wager the:\nA. Color\nB. Odd or Even\nC. High or Low\nD. Color and Number\nE. Quit\n\n")).lower()

            if shift == "a":
                self.wager_color()

            elif shift == "e":
                print("Thank you for playing! Your total winnings are: $", self.bank)
                pa = str(input("Would you like to return to the casino floor?")).lower()
                if pa == "yes" or pa == "y":
                    return self.bank
                else:
                    print("Thank you for playing!!")
                    break

            elif shift == "b":
                self.wager_odd_or_even()

            elif shift == "c":
                self.high_or_low()

            elif shift == "d":
                self.color_and_number()

            else:
                print("Please select from the above.\n")

