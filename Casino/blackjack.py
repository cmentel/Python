'''
Connor Mentel
Blackjack
Last Mod: 8/4/20
'''

import random

DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4


class Blackjack:
    def __init__(self, bank):
        self.bank = bank
        self.player_total = 0
        self.dealer_total = 0
        self.bet = 0
        self.player_hand = random.sample(DECK, 2)
        self.dealer_hand = random.sample(DECK, 2)
        self.bet_already = False

    # method to get random card for hand
    def deal(self, hand):
        card = random.sample(DECK, 1)[0]
        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 14:
            card = "A"
        hand.append(card)

    # method to update totals
    def get_totals(self):
        player_total = 0
        for card in self.player_hand:
            if card == "J" or card == "Q" or card == "K":
                player_total += 10
            elif card == "A":
                if player_total >= 11:
                    player_total += 1
                else:
                    player_total += 11
            else:
                player_total += card

        self.player_total = player_total

        dealer_total = 0
        for card in self.dealer_hand:
            if card == "J" or card == "Q" or card == "K":
                dealer_total += 10
            elif card == "A":
                if dealer_total >= 11:
                    dealer_total += 1
                else:
                    dealer_total += 11
            else:
                dealer_total += card

        self.dealer_total = dealer_total

    # method to print game mid game
    def print_game(self):
        print("The dealer has a " + str(self.dealer_hand[0]))
        print("You have a " + str(self.player_hand) + " for a total of " + str(self.player_total))

    # method to print hands and values
    def print_game_end(self):
        print("The dealer has a " + str(self.dealer_hand) + " for a total of " + str(self.dealer_total))
        print("You have a " + str(self.player_hand) + " for a total of " + str(self.player_total))

    def options(self):
        self.get_totals()
        # if haven't bet yet
        while not self.bet_already:
            try:
                print("What's your bet?\nYou have:", self.bank)
                bet = int(input())
                self.bet = bet
                self.bank -= bet
                self.bet_already = True
                break
            except:
                continue
        else:
            pass

        print("The dealer is showing a", self.dealer_hand[0])
        print("You have a " + str(self.player_hand) + " for a total of " + str(self.player_total))

        playing = True
        while playing:
            self.get_totals()

            # if blackjack
            if self.player_total == 21:
                print("BLACKJACK!!\n")
                self.bank = self.bank + (self.bet * 2.5)
                playing = False
                break

            print("What would you like to do?\n")
            choice = str(input("1. Hit\n2. Stand\n3. Quit:\n"))

            if choice == "1":
                self.deal(self.player_hand)
                self.get_totals()
                self.print_game()
                if self.player_total > 21:
                    print("You busted")
                    playing = False
                    break

            elif choice == "2":
                while self.dealer_total < 17:
                    self.get_totals()
                    self.deal(self.dealer_hand)

                self.print_game_end()
                if self.player_hand == 21:
                    print("Congratulations! You got a Blackjack!\n")
                    self.bank = self.bank + int(self.bet * 2.5)
                elif self.dealer_total == 21:
                    print("Sorry, you lose. The dealer got a blackjack.\n")
                elif self.player_total > 21:
                    print("Sorry. You busted. You lose.\n")
                elif self.dealer_total > 21:
                    print("Dealer busts. You win!\n")
                    self.bank = self.bank + int(self.bet * 2)
                elif self.player_total < self.dealer_total:
                    print("Sorry. Your score isn't higher than the dealer. You lose.\n")
                elif self.player_total > self.dealer_total:
                    print("Congratulations. Your score is higher than the dealer. You win\n")
                    self.bank = self.bank + int(self.bet * 1.5)
                elif self.player_total == self.dealer_total:
                    print("It's a tie! No money won or lost!\n")
                    self.bank += self.bet
                playing = False
                break
