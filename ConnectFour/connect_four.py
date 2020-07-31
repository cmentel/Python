'''
Connor Mentel
Anti Gravity Connect Four
Last mod: 7/30/20
'''

# assign the spots
EMPTY = "|_|"
PLAYER_ONE = " X "
PLAYER_TWO = " O "


# getting player names
player_one_name = input("Hello! What is player one's name?\n")
player_two_name = input("Hello! What is player two's name?\n")


# function to print the board
def board_print(board):
    print("         GAME BOARD:    ")
    holder = 1
    counter = 1
    top_numbers = []
    for row in board:
        if holder == 1:
            for spot in row:
                top_numbers.append(counter)
                counter += 1
            print("  ",
                  str(top_numbers).replace("[", "").replace("]", "").replace(",", "|").replace("'", "").replace("|",
                                                                                                                "  "))
        print(" ",
              str(row).replace("[", "").replace("]", "").replace("'", "").replace("||", "|").replace(",", ""))

        holder += 1


# function to check if game is over per row
def for_spot_in_row(row, column):
    for spot in row:
        try:
            if is_game_over_helper(row, column):
                return True
        except:
            pass


# function to get the winner of the game
def get_winner(player, board):
    if is_game_over_full_board(board):
        print("------------ GAME OVER!! BOARD IS FULL!! ------------\n")
        board_print(board)
        return
    print("------------ GAME OVER!!", player.upper(), "WINS!! ------------\n")
    if is_game_over_diagonal(board):
        print(player, "got connect four in a diagonal!\n")
    if is_game_over_vertical(board):
        print(player, "got connect four in a vertical!\n")
    if is_game_over_horizontal(board):
        print(player, "got connect four in a horizontal!\n")
    board_print(board)


# function to check if game is over for a full board
def is_game_over_full_board(board):
    for row in board:
        for spot in row:
            if spot == "|_|":
                return False

    return True


# function to check if game is over given four consecutive spots
def is_game_over_helper(row, column):
    for i in row:
        try:
            if (((row)[column] == (row)[column + 1]) and ((row)[column] == (row)[column + 2]) and (
                    (row)[column] == (row)[column + 3]) and (row)[column] != EMPTY) or \
                    (((row)[column + 1] == (row)[column + 2]) and ((row)[column + 1] == (row)[column + 3]) and (
                            (row)[column + 1] == (row)[column + 4]) and (row)[column + 1] != EMPTY) or \
                    (((row)[column + 2] == (row)[column + 3]) and ((row)[column + 2] == (row)[column + 4]) and (
                            (row)[column + 2] == (row)[column + 5]) and (row)[column + 2] != EMPTY) or \
                    (((row)[column + 3] == (row)[column + 4]) and ((row)[column + 3] == (row)[column + 5]) and (
                            (row)[column + 3] == (row)[column + 6]) and (row)[column + 3] != EMPTY):
                return True
        except:
            pass


# function to check if the game is over for a horizontal win
def is_game_over_horizontal(board):
    # check for four in the same row
    row_hold = 0
    for row in board:
        column = 0
        for spot in row:
            try:
                if is_game_over_helper(row, column):
                    return True
            except:
                pass
            column += 1
        row_hold += 1


# function to check if the game is over for a vertical win
def is_game_over_vertical(board):
    row_hold = 0
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    for row in board:
        column = 0
        for spot in row:
            try:
                if column == 0:
                    one.append((row)[column])
                elif column == 1:
                    two.append((row)[column])
                elif column == 2:
                    three.append((row)[column])
                elif column == 3:
                    four.append((row)[column])
                elif column == 4:
                    five.append((row)[column])
                elif column == 5:
                    six.append((row)[column])
                elif column == 6:
                    seven.append((row)[column])
            except:
                pass

            if for_spot_in_row(one, column) or \
                    for_spot_in_row(two, column) or \
                    for_spot_in_row(three, column) or \
                    for_spot_in_row(four, column) or \
                    for_spot_in_row(five, column) or \
                    for_spot_in_row(six, column) or \
                    for_spot_in_row(seven, column):
                return True
            column += 1
        row_hold += 1


# function to check if the game is over for a diagonal win
def is_game_over_diagonal(board):
    # check for four in the same diagonal
    row_hold = 0
    holder = []
    for row in board:
        column = 0
        for spot in row:
            try:
                holder.append(row[column])
            except:
                pass
            column += 1
        row_hold += 1

    count = 0
    player_one_index = []
    player_two_index = []
    for i in holder:
        if i == PLAYER_ONE:
            if count not in player_one_index:
                player_one_index.append(count)

        elif i == PLAYER_TWO:
            if count not in player_two_index:
                player_two_index.append(count)
        count += 1

    if check_indexes(player_one_index) or check_indexes(player_two_index):
        return True

    return False


# helper function to check if diagonal is successful
def check_indexes(list_of_indexes):
    diagonal_hold_8 = []
    diagonal_hold_6 = []

    try:
        for i in range(len((list_of_indexes))):
            temp = list_of_indexes[i]
            # 8 spots away from each other
            if (temp in list_of_indexes and
                    temp + 8 in list_of_indexes and
                    temp + 16 in list_of_indexes and
                    temp + 24 in list_of_indexes and
                    [temp, temp + 8, temp + 16, temp + 24] not in diagonal_hold_8):
                diagonal_hold_8.append([temp, temp + 8, temp + 16, temp + 24])

                # 6 spots away from each other
            if (temp in list_of_indexes and
                    temp + 6 in list_of_indexes and
                    temp + 12 in list_of_indexes and
                    temp + 18 in list_of_indexes and
                    [temp, temp + 6, temp + 12, temp + 18] not in diagonal_hold_6):
                diagonal_hold_6.append([temp, temp + 6, temp + 12, temp + 18])

        for array8 in diagonal_hold_8:
            if diagonal_helper(array8):
                return True

        for array6 in diagonal_hold_6:
            if diagonal_helper(array6):
                return True

    except:
        pass

    return False


# diagonal helper function
def diagonal_helper(array):
    # if empty
    if not array:
        return False

    holder = []
    for spot in array:
        if spot <= 6:
            holder.append(1)
        elif spot >= 7 and spot <= 13:
            holder.append(2)
        elif spot >= 14 and spot <= 20:
            holder.append(3)
        elif spot >= 21 and spot <= 27:
            holder.append(4)
        elif spot >= 28 and spot <= 34:
            holder.append(5)
        elif spot >= 35 and spot <= 41:
            holder.append(6)

    return holder_check(holder)


# function to check if the holder array has four valid diagonal connections
def holder_check(holder):
    for i in range(len(sorted(holder))):
        try:
            # return false if holder does not have four numbers.
            if len(holder) < 4:
                return False

            # return false if any in diagonal array are in same row.
            if holder[i] == holder[i + 1]:
                return False

            # return false if any in diagonal array are not consecutive.
            if holder[i] - holder[i + 1] != -1:
                return False

        except:
            continue
    return True


# function to check if the game is over
def is_game_over(board):
    if is_game_over_horizontal(board) or is_game_over_vertical(board) or is_game_over_diagonal(
            board) or is_game_over_full_board(board):
        return True

    return False


# function to accept moves from each player
def move(board, player_turn):
    turn = True
    while turn:
        try:
            print(player_turn, "please input your move by entering the column\n")
            player_move = input()
            try:
                player_move = (int(player_move))
            except:
                pass

            # if value is off the board
            if player_move > 7 or player_move < 1:
                print("Invalid move, please try again!\n")



            player_move = player_move - 1

            # if column is filled
            if board[0][player_move] != EMPTY:
                print("Invalid move, please try again!\n")

            # moves to empty spot
            try:
                row_count = 5
                for row in board:

                    if board[row_count][player_move] == EMPTY and player_turn == player_one_name:
                        board[row_count][player_move] = PLAYER_ONE
                        turn = False
                        break

                    elif board[row_count][player_move] == EMPTY and player_turn == player_two_name:
                        board[row_count][player_move] = PLAYER_TWO
                        turn = False
                        break

                    else:
                        row_count -= 1
                        continue

            except:
                pass

        except:
            pass


# function to play the game
def play(board, player_one, player_two):
    playing = True
    while playing:
        board_print(board)
        move(board, player_one)
        if is_game_over(board):
            playing = False
            get_winner(player_one, board)
            break
        board_print(board)
        move(board, player_two)
        if is_game_over(board):
            playing = False
            get_winner(player_two, board)
            break


# initializes and launches the game
def initialize():
    height = 6
    width = 7
    board = [[EMPTY] * 7 for i in range(6)]

    print("Welcome,", player_one_name, "&", player_two_name, "!\n")
    play(board, player_one_name, player_two_name)

    print("Good game", player_one_name, "&", player_two_name, "!\n")
    print("Do you want to play again? (Y or N)\n")
    again = input().lower()
    if again == "y" or again == "yes":
        initialize()
    else:
        exit("Thanks for playing! :-)")


initialize()
