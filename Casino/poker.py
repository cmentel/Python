'''
Connor Mentel
Poker
Last Mod: 7/31/20
'''
import random
from collections import defaultdict
from itertools import combinations

VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

CARD_ORDER_DICT = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}

DECK = ["AH", "AS", "AC", "AD", "KH", "KS", "KC", "KD", "QH", "QS", "QC", "QD", "JH", "JS", "JC", "JD", "TH", "TS",
        "TC", "TD", "9H", "9S", "9C", "9D", "8H", "8S", "8C", "8D", "7H", "7S", "7C", "7D", "6H", "6S", "6C", "6D",
        "5H", "5S", "5C", "5D", "4H", "4S", "4C", "4D", "3H", "3S", "3C", "3D", "2H", "2S", "2C", "2D"]

HAND_DICT = {9: "straight-flush", 8: "four-of-a-kind", 7: "full-house", 6: "flush", 5: "straight", 4: "three-of-a-kind",
             3: "two-pairs", 2: "one-pair", 1: "highest-card"}


# function to print the hand given cards
def print_hand(cards):
    print("            1  2  3  4  5 ")
    print("YOUR HAND:", str(cards).replace("[", "").replace("]", "").replace("'", "").replace(",", ""), "\n")


# functions to print all the hands on the table after gambling
def print_hands(player_hand, dealer_hand, table_hand):
    print("YOUR HAND:", str(player_hand).replace("[", "").replace("]", "").replace("'", "").replace(",", ""),
          "\nYour max hand was a", play(player_hand, table_hand))
    print("DEALER HAND:", str(dealer_hand).replace("[", "").replace("]", "").replace("'", "").replace(",", ""),
          "\nDealer's max hand was a", play(dealer_hand, table_hand))
    print("TABLE:", str(table_hand).replace("[", "").replace("]", "").replace("'", "").replace(",", ""), "\n")


# function to initialize deck and hands
def initialize(bank):
    cards = random.sample(DECK, 15)
    player_hand = cards[:5]
    table_hand = cards[5:10]
    dealer_hand = cards[10:]
    return options(bank, cards)


# function to get the values associated with the hands
def get_value(val):
    for key, value in HAND_DICT.items():
        if val == value:
            return key


# function to swap out cards
def swap(player_hand):
    cards_to_swap = input("Please enter the individual number of each card you'd like to swap.\nex: 1 3 4\n")
    swaps = []
    holder = 0

    counter = 0
    try:
        if int(cards_to_swap) > 5:
            print("Please enter values from 1 - 5\n")
            swap(player_hand)

        # TODO Implement error catching for string not including decimal

    except:
        pass

    for i in cards_to_swap:
        counter += 1
        try:
            if int(i) > 5:
                print("Please enter values from 1 - 5\n")
                swap(player_hand)
            elif counter > 5:
                print("Please enter only five values from 1 - 5\n")
                swap(player_hand)

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
        player_hand[int(proper_spot)] = "#"

    count = 0
    for i in range(len(player_hand)):
        if player_hand[i] == "#":
            player_hand[i] = swap_start[count]
            count += 1
        else:
            pass

    return player_hand


# function to place bet
def bet(bank):
    try:
        bet_number = int(input("How much would you like to bet?\n"))
        print("bet number",bet_number)
        print("bank", bank)
        if bet_number > bank:
            print("Your bet cannot be greater than your bank\n")
            bet(bank)
        else:
            return bet_number
    except:
        print("Please enter a number.\n")
        bet(bank)


# function to wager and play outcome
def gamble(bank, player_hand, dealer_hand, table_hand):
    player_outcome = play(player_hand, table_hand)
    dealer_outcome = play(dealer_hand, table_hand)

    player_value = get_value(player_outcome)
    dealer_value = get_value(dealer_outcome)

    if player_value > dealer_value:
        return "Player"
    elif player_value < dealer_value:
        return "Dealer"
    else:
        return "Tie"


# helper function to get the options of poker
def sub_options(bank, player_hand, dealer_hand, table_hand, bet_holder, swap_already, bet_already):
    if bank <= 0:
        print("Sorry you're broke!\n")
        return bank

    choice = str(input("Enter number:\n1. Swap\n2. Bet\n3. Play\n4. Check Bank\n5. Exit\n"))

    # swapping
    if choice == "1" and swap_already == False:
        swap_already = True
        player_hand = swap(player_hand)
        print_hand(player_hand)
        sub_options(bank, player_hand, dealer_hand, table_hand, bet_holder, swap_already, bet_already)

    # betting
    elif choice == "2" and bet_already == False:
        bet_already = True
        bet_holder = bet(bank)
        sub_options(bank, player_hand, dealer_hand, table_hand, bet_holder, swap_already, bet_already)

    # gamble
    elif choice == "3":
        winner = gamble(bank, player_hand, dealer_hand, table_hand)
        if winner == "Player":
            bank = bank + (bet_holder * 2)
            print("Congrats!! You won!\n")
            print_hands(player_hand, dealer_hand, table_hand)
            print("player bank",bank)
        elif winner == "Dealer":
            bank = bank - bet_holder
            print("Sorry you didn't win this time!\n")
            print_hands(player_hand, dealer_hand, table_hand)
            print("dealer bank",bank)
        else:
            print("It's a tie! Nothing changes!\n")
            print_hands(player_hand, dealer_hand, table_hand)
            print("tie bank", bank)
            bank = bank + bet_holder
        print("final bank", bank)
        return bank

    # check bank
    elif choice == "4":
        print("Your bank is:", bank - bet_holder)
        sub_options(bank, player_hand, dealer_hand, table_hand, bet_holder, swap_already, bet_already)


    # exit
    elif choice == "5":
        print("Thanks for playing poker!!\n")
        to_be_ret = "Exit" + str(bank)
        return to_be_ret

    else:
        print("You can't do that right now!\nIf you can't select an option you have to Play!\n")
        sub_options(bank, player_hand, dealer_hand, table_hand, bet_holder, swap_already, bet_already)


# options to play the game
def options(bank, cards):
    player_hand = cards[:5]
    table_hand = cards[5:10]
    dealer_hand = cards[10:]

    swap_already = False
    bet_already = False

    bet_holder = 0
    print("What would you like to do with your hand below?\n")
    print_hand(player_hand)
    # prompt to bet
    if bet_holder == 0:
        print("(Hint: You haven't bet yet, I'd consider betting before playing!)\n")

    playing = True
    while playing:
        #TODO always returns "None"
        result = str(sub_options(bank, player_hand, dealer_hand, table_hand, bet_holder, swap_already, bet_already))
        print("result",result)

        # if we exited out of poker
        if "Exit" in result:
            final_bank = result.lstrip("Exit")
            playing = False
            return final_bank

        # if error in getting bank
        elif result == "None":
            print("NONE")
            initialize(bank)

        # if bank is empty
        elif int(result) <= 0:
            playing = False
            print("Get out of my casino you broke pig! 🐷\n")
            break

        # if continuing to play
        else:
            bank = int(result)
            print(bank)
            initialize(bank)


# function to check the value of the hand
def check_hand(hand):
    if check_straight_flush(hand):
        return 9
    if check_four_of_a_kind(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pair(hand):
        return 3
    if check_two_pairs(hand):
        return 3
    if check_pair(hand):
        return 2
    if check_one_pairs(hand):
        return 2
    return 1


# gets best hand from own hand and table
def play(player_hand, table_hand):
    best_hand = 0
    for i in range(6):
        possible_combos = combinations(player_hand, 5 - i)
        for c in possible_combos:
            current_hand = list(c) + table_hand[:i]
            hand_value = check_hand(current_hand)
            if hand_value > best_hand:
                best_hand = hand_value

    return HAND_DICT[best_hand]


# checks for a straight flush
def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False


# checks for four of a kind
def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 4]:
        return True
    return False


# checks for two pairs
def check_two_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 2, 2]:
        return True
    return False


# check for a pair
def check_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 1, 1, 2]:
        return True
    return False


# check for a full house
def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2, 3]:
        return True
    return False


# check for a flush
def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


# check for a straight
def check_straight(hand):
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
def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if set(value_counts.values()) == {3, 1}:
        return True
    else:
        return False


# check for two pairs
def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 2, 2]:
        return True
    else:
        return False


# check for one pair
def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():
        return True
    else:
        return False
