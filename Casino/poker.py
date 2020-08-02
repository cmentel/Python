'''
Connor Mentel
Poker
Last Mod: 8/2/20
'''

import random
from collections import defaultdict
from itertools import combinations

VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
          "A": 14}

CARD_ORDER_DICT = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
                   "K": 13,
                   "A": 14}

DECK = ["AH", "AS", "AC", "AD", "KH", "KS", "KC", "KD", "QH", "QS", "QC", "QD", "JH", "JS", "JC", "JD", "TH", "TS",
        "TC", "TD", "9H", "9S", "9C", "9D", "8H", "8S", "8C", "8D", "7H", "7S", "7C", "7D", "6H", "6S", "6C", "6D",
        "5H", "5S", "5C", "5D", "4H", "4S", "4C", "4D", "3H", "3S", "3C", "3D", "2H", "2S", "2C", "2D"]

HAND_DICT = {9: "straight-flush", 8: "four-of-a-kind", 7: "full-house", 6: "flush", 5: "straight",
             4: "three-of-a-kind",
             3: "two-pairs", 2: "one-pair", 1: "highest-card"}


class Poker:

    # method to initialize deck and hands
    def __init__(self, bank):
        self.cards = random.sample(DECK, 15)
        self.player_hand = self.cards[:5]
        self.table_hand = self.cards[5:10]
        self.dealer_hand = self.cards[10:]
        self.swap_already = False
        self.bet_already = False
        self.finished = False
        self.bet_hold = 0
        self.bank = bank

    # method to print the hand given cards
    def print_hand(self, hand):
        print("            1  2  3  4  5 ")
        print("YOUR HAND:", str(hand).replace("[", "").replace("]", "").replace("'", "").replace(",", ""), "\n")

    # method to print all the hands on the table after gambling
    def print_hands(self):
        print("YOUR HAND:", str(self.player_hand).replace("[", "").replace("]", "").replace("'", "").replace(",", ""),
              "\nYour max hand was a", self.play(self.player_hand))
        print("DEALER HAND:",
              str(self.dealer_hand).replace("[", "").replace("]", "").replace("'", "").replace(",", ""),
              "\nDealer's max hand was a", self.play(self.dealer_hand))
        print("TABLE:", str(self.table_hand).replace("[", "").replace("]", "").replace("'", "").replace(",", ""), "\n")

    # method to get the values associated with the hands
    def get_value(self, outcome):
        for key, value in HAND_DICT.items():
            if outcome == value:
                return key

    # function to swap out cards
    def swap(self):
        swapping = True
        while swapping:
            # self.print_hand(self.player_hand)
            cards_to_swap = input("Please enter the individual number of each card you'd like to swap.\nex: 1 3 4\n")
            swaps = []
            holder = 0

            counter = 0
            try:
                int(cards_to_swap)
                if int(cards_to_swap) > 5:
                    print("Please enter values from 1 - 5\n")
                    continue

            except:
                print("Please enter values from 1 - 5\n")

            for i in cards_to_swap:
                counter += 1
                try:
                    if int(i) > 5:
                        print("Please enter values from 1 - 5\n")
                        continue
                    elif counter > 5:
                        print("Please enter only five values from 1 - 5\n")
                        continue

                    swaps.append(int(i))
                    holder += 1
                except:
                    pass

            swap_cards = random.sample(DECK, holder)
            swap_start = []

            for i in range(len(swap_cards)):
                try:
                    swap_start.append(str(swap_cards[i]))
                except:
                    pass

            for i in swaps:
                proper_spot = int(i - 1)
                self.player_hand[int(proper_spot)] = "#"

            count = 0
            for i in range(len(self.player_hand)):
                if self.player_hand[i] == "#":
                    self.player_hand[i] = swap_start[count]
                    count += 1
                else:
                    pass
            swapping = False
            break

    # function to place bet
    def bet(self):
        betting = True
        while betting:
            try:
                bet_number = int(input("How much would you like to bet?\n"))
                if bet_number > self.bank:
                    print("Your bet cannot be greater than your bank\n")
                    continue
                elif bet_number <= 0:
                    print("Your bet must be a positive number!\n")
                    continue
                else:
                    self.bet_hold = bet_number
                    self.bank = self.bank - self.bet_hold
                    betting = False
                    break
            except:
                print("Please enter a number.\n")
                continue

    # function to wager and play outcome
    def gamble(self):
        player_outcome = self.play(self.player_hand)
        dealer_outcome = self.play(self.dealer_hand)

        player_value = self.get_value(player_outcome)
        dealer_value = self.get_value(dealer_outcome)

        if player_value > dealer_value:
            return "Player"
        elif player_value < dealer_value:
            return "Dealer"
        else:
            return "Tie"

    # options to play the game
    def options(self):
        print("What would you like to do with your hand below?\n")
        self.print_hand(self.player_hand)

        playing = True
        while playing:
            if self.bank <= 0:
                print("Sorry you're broke!\n")
                return self.bank
            choice = str(input("Enter number:\n1. Swap\n2. Bet\n3. Play\n4. Check Bank\n5. Exit\n"))

            # error catch invalid input
            try:
                int(choice)
            except:
                print("Please enter a valid option from 1 to 5\n")
                continue

            # swapping
            if choice == "1" and self.swap_already == False:
                self.swap_already = True
                self.swap()
                self.print_hand(self.player_hand)
                continue

            # betting
            elif choice == "2" and self.bet_already == False:
                self.bet_already = True
                self.bet()
                continue

            # gamble
            elif choice == "3":
                winner = self.gamble()
                if self.bet_hold == 0:
                    print("You need to bet before playing!\n")
                    continue
                if winner == "Player":
                    self.bank = self.bank + (self.bet_hold * 2)
                    print("Congrats!! You won!\n")
                    self.print_hands()
                    return self.bank
                elif winner == "Dealer":
                    print("Sorry you didn't win this time!\n")
                    self.print_hands()
                    return self.bank - self.bet_hold
                else:
                    print("It's a tie! Nothing changes!\n")
                    self.print_hands()
                    self.bank = self.bank + self.bet_hold
                    return self.bank

            # check bank
            elif choice == "4":
                print("Your bank is:", self.bank)
                continue


            # exit
            elif choice == "5":
                print("Thanks for playing poker!!\n")
                self.finished = True
                options = False
                return self.bank

            # invalid option input
            elif int(choice) > 5 or int(choice) < 1:
                print("Please enter a valid option from 1 to 5\n")
                continue

            # forced options
            else:
                if self.bet_already == True:
                    print("You already bet!\n")
                if self.swap_already == True:
                    print("You already swapped!\n")
                print("If you can't select an option you have to Play!\n")
                continue

        return self.bank

    # function to check the value of the hand
    def check_hand(self, hand):
        if self.check_straight_flush(hand):
            return 9
        if self.check_four_of_a_kind(hand):
            return 8
        if self.check_full_house(hand):
            return 7
        if self.check_flush(hand):
            return 6
        if self.check_straight(hand):
            return 5
        if self.check_three_of_a_kind(hand):
            return 4
        if self.check_two_pair(hand):
            return 3
        if self.check_two_pairs(hand):
            return 3
        if self.check_pair(hand):
            return 2
        if self.check_one_pairs(hand):
            return 2
        return 1

    # gets best hand from own hand and table
    def play(self, hand):
        best_hand = 0
        for i in range(6):
            possible_combos = combinations(hand, 5 - i)
            for c in possible_combos:
                current_hand = list(c) + self.table_hand[:i]
                hand_value = self.check_hand(hand)
                if hand_value > best_hand:
                    best_hand = hand_value

        return HAND_DICT[best_hand]

    # checks for a straight flush
    def check_straight_flush(self, hand):
        if self.check_flush(hand) and self.check_straight(hand):
            return True
        else:
            return False

    # checks for four of a kind
    def check_four_of_a_kind(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if sorted(value_counts.values()) == [1, 4]:
            return True
        return False

    # checks for two pairs
    def check_two_pair(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if sorted(value_counts.values()) == [1, 2, 2]:
            return True
        return False

    # check for a pair
    def check_pair(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if sorted(value_counts.values()) == [1, 1, 1, 2]:
            return True
        return False

    # check for a full house
    def check_full_house(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if sorted(value_counts.values()) == [2, 3]:
            return True
        return False

    # check for a flush
    def check_flush(self, hand):
        suits = [i[1] for i in hand]
        if len(set(suits)) == 1:
            return True
        else:
            return False

    # check for a straight
    def check_straight(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        rank_values = [CARD_ORDER_DICT[i] for i in values]
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range == 4):
            return True
        else:
            # check straight with low Ace
            if set(values) == {"A", "2", "3", "4", "5"}:
                return True
            return False

    # check for three of a kind
    def check_three_of_a_kind(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if set(value_counts.values()) == {3, 1}:
            return True
        else:
            return False

    # check for two pairs
    def check_two_pairs(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if sorted(value_counts.values()) == [1, 2, 2]:
            return True
        else:
            return False

    # check for one pair
    def check_one_pairs(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if 2 in value_counts.values():
            return True
        else:
            return False
