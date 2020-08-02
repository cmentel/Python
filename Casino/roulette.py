'''
Connor Mentel
Roulette
Last mod: 8/2/20
'''

import random

ROULETTE_COLORS = ["Black", "Red"]
ROULETTE_TVALUES = ["Odd", "Even"]
ROULETTE_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
ROULETTE_RED_NUMS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
ROULETTE_BLACK_NUMS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


class Roulette:
    def __init__(self, bank):
        self.bank = bank
        self.options()

    def options(self):
        playing = True
        while playing == True:
            shift = input(
                "Would you like to wager the:\nA. Color\nB. Odd or Even\nC. High or Low\nD. Color and Number\nE. Quit\n\n")

            if shift.lower == "a":
                r_bet = int(input("How much would you like to wager?\n"))
                self.bank = self.bank - r_bet
                r_color = input("What color would you like to bet? 'Red' or 'Black' ?\n")
                r_color = r_color.capitalize()
                print("Rolling Rolling Rolling...")
                a_color = random.choice(ROULETTE_COLORS)
                a_color = a_color.capitalize()
                print("The rolled color is:", a_color)
                if a_color == r_color:
                    print("Congrats you won!")
                    bank = self.bank + (r_bet * 2)
                    print("Your current bank is:", self.bank)

                else:
                    print("You didn't win this time! Try again!")
                    print("Your current bank is:", self.bank)

            elif shift.lower == "e":
                print("Thank you for playing! Your total winnings are: $", self.bank)
                pa = input("Would you like to return to the casino floor?")
                if pa.lower() == "yes":
                    return self.bank
                else:
                    print("Thank you for playing!!")
                    break

            elif shift.lower() == "b":
                r_bet = int(input("How much would you like to wager?\n"))
                self.bank = self.bank - r_bet
                r_value = input("Do you guess 'Odd' or 'Even' ?\n")
                r_value = r_value.capitalize()
                print("Rolling Rolling Rolling...")
                e_value = random.choice(ROULETTE_TVALUES)
                e_value = e_value.capitalize()
                print("The rolled value is:", e_value)
                if e_value == r_value:
                    print("Congrats you won!")
                    self.bank = self.bank + (r_bet + r_bet)
                    print("Your current bank is:", self.bank)
                else:
                    print("You didn't win this time! Try again!")
                    print("Your current bank is:", self.bank)

            elif shift.lower == "c":
                r_bet = int(input("How much would you like to wager?\n"))
                self.bank = self.bank - r_bet
                r_value = input("Do you guess 'High' or 'Low'?\n")
                r_value = r_value.capitalize()
                print("Rolling Rolling Rolling...")
                c_value = random.choice(ROULETTE_VALUES)
                print("The rolled number is:", c_value)
                if r_value == "High" or r_value == "high":
                    if c_value > 18:
                        print("Congrats you won!")
                        self.bank = self.bank + (r_bet * 2)
                        print("Your current bank is:", self.bank, "\n")
                    else:
                        print("You didn't win this time! Try again!")
                        print("Your current bank is:", self.bank, "\n")
                elif r_value == "Low" or r_value == "low":
                    if c_value <= 18:
                        print("Congrats you won!")
                        bank = self.bank + (r_bet * 2)
                        print("Your current bank is:", self.bank, "\n")
                    else:
                        print("You didn't win this time! Try again!")
                        print("Your current bank is:", self.bank, "\n")

            elif shift.lower() == "d":
                r_bet = int(input("How much would you like to wager?\n"))
                self.bank = self.bank - r_bet
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

                    if r_color.lower() == "black":
                        r_value = int(input("What number do you guess?\n"))
                        if r_value not in ROULETTE_BLACK_NUMS:
                            print("That number is not black. Please select again.\n")
                        else:
                            print("Rolling Rolling Rolling...\n")
                            d_color = random.choice(ROULETTE_RED_NUMS)
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

            else:
                print("Please select from the above.\n")

            if self.bank <= 0:
                print("Sorry you're broke! Have a great night!")
                return self.bank
