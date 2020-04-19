"""
TEST
Connor Mentel
CS 5001
HW 2
Programming #2
Defining Functions
"""


# Function 1a (Separated because we need a version to test the function.)
def absolute(absolute_1):
    print("Hi! Welcome to the absolute value calculator!")
    # absolute_1 = int(input("What number would you like to know the absolute value of? "))

    print("You selected ", int(absolute_1))
    if (int(absolute_1) > 0):
        print("The absolute value of your number is, ")
        return int(absolute_1)

    elif (int(absolute_1) < 0):
        print("The absolute value of your number is, ")
        return int(absolute_1 * -1)

    else:
        print("That absolute value of 0 is 0! How cool!")
        return 0


# Function 1b (Separated because we need a version that prompts the user.)
def absolute2():
    print("Hi! Welcome to the absolute value calculator!")
    absolute_1 = int(input("What number would you like to know the absolute value of? "))

    print("You selected ", int(absolute_1))
    if (int(absolute_1) > 0):
        print("The absolute value of your number is, ", int(absolute_1))
        return int(absolute_1)

    elif (int(absolute_1) < 0):
        print("The absolute value of your number is, ", int(absolute_1 * -1))
        return int(absolute_1 * -1)

    else:
        print("That absolute value of 0 is 0! How cool!")
        return 0


# Function 2a (Separated because we need a version that prompts the user.)
def manhattan():
    print('''\nHi! Welcome to the Manhattan distance calculator!\nI'm going to ask you for four coordinates ''')
    x1, y1, x2, y2 = input(
        '''Please enter the coordinates of the two destinations such that your first answer will be the x coordinate of destination 1, your second will be y1, third x2, fourth y2, all separated by spaces. ''').split()
    print("\nGreat! Thank you!")

    # if x2 - x1 is less than 0 and if y2 - y1 is less than 0
    if (((int(x2) - int(x1))) < 0) and ((int(y2) - int(y1)) < 0):
        print("\nThe distance between these destinations is, ",
              (((int(x2) - int(x1)) * -1 + ((int(y2) - int(y1))) * -1)))

    # if x2-x1 is less than 0
    elif (((int(x2) - int(x1))) < 0):
        print("\nThe distance between these destinations is, ",
              (((int(x2) - int(x1)) * -1)) + (((int(y2) - int(y1)))))

    # if y2-y1 is less than 0
    elif (((int(y2) - int(y1))) < 0):
        print("\nThe distance between these destinations is, ",
              (((int(x2) - int(x1)))) + (((int(y2) - int(y1)) * -1)))

    # if neither absolute is less than 0
    elif (((int(x2) - int(x1)) + (int(y2) - int(y1))) > 0):
        print("\nThe distance between these destinations is, ",
              ((int(x2) - int(x1) + (int(y2) - int(y1)))))

    # if the destinations are in the same location
    else:
        print("These are in the same location!")


# Function 2b (Separated because we need a version to test the function.)
def manhattan2(x1, y1, x2, y2):
    print('''\nHi! Welcome to the Manhattan distance calculator!\nI'm going to ask you for four coordinates ''')
    # x1,y1,x2,y2 = input('''Please enter the coordinates of the two destinations such that your first answer will be the x coordinate of destination 1, your second will be y1, third x2, fourth y2, all separated by spaces. ''').split()
    print("\nGreat! Thank you!")

    print(x1, y1, x2, y2)
    # if x2 - x1 is less than 0 and if y2 - y1 is less than 0
    if (((int(x2) - int(x1))) < 0) and ((int(y2) - int(y1)) < 0):
        print("\nThe distance between these destinations is, ")
        return (((int(x2) - int(x1)) * -1 + ((int(y2) - int(y1))) * -1))

    # if x2-x1 is less than 0
    elif (((int(x2) - int(x1))) < 0):
        print("\nThe distance between these destinations is, ")
        return ((((int(x2) - int(x1)) * -1)) + (((int(y2) - int(y1)))))

    # if y2-y1 is less than 0
    elif (((int(y2) - int(y1))) < 0):
        print("\nThe distance between these destinations is, ")
        return ((((int(x2) - int(x1)))) + (((int(y2) - int(y1)) * -1)))

    # if neither absolute is less than 0
    elif (((int(x2) - int(x1)) + (int(y2) - int(y1))) > 0):
        print("\nThe distance between these destinations is, ")
        return ((int(x2) - int(x1) + (int(y2) - int(y1))))

    # if the destinations are in the same location
    else:
        print("These are in the same location!")
        return 0


# Function 3a (Separated because we need a version to test the function.)
def euclidean(e, f, g, h):
    print('''Hi! welcome to the Euclidean Manhattan distance calculator!\nI'm going to ask you for four coordinates''')
    # e,f,g,h = input('''Please enter the coordinates of the two destinations such that your first answer will be the x coordinate of destination 1, your second will be y1, third x2, fourth y2, all separated by spaces.''').split()

    print("\nGreat! Thank you!")
    e_Var = round(((((float(g) - float(e))) * (float(g) - (float(e)))) +
                   (((float(h) - float(f))) * (float(h) - float(f)))) ** .5, 2)
    print("\nThe Euclidean distance between these two points is, ", e_Var)
    return e_Var


# Function 3b (Separated because we need a version that prompts the user.)
def euclidean2():
    print('''Hi! welcome to the Euclidean Manhattan distance calculator!\nI'm going to ask you for four coordinates''')
    e, f, g, h = input(
        '''Please enter the coordinates of the two destinations such that your first answer will be the x coordinate of destination 1, your second will be y1, third x2, fourth y2, all separated by spaces.''').split()

    print("\nGreat! Thank you!")
    e_Var2 = round(((((float(g) - float(e))) * (float(g) - (float(e)))) +
                    (((float(h) - float(f))) * (float(h) - float(f)))) ** .5, 2)
    print("\nThe Euclidean distance between these two points is, ", e_Var2)
    return e_Var2
