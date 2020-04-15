"""
Connor Mentel
CS 5002 - Foundations
Programming #1
upc.py
"""

# Test UPC number 1: 073854008089
# Test UPC number 2: 796030114977

def is_valid_upc ():
    Final = []
    ODDSby3 = []
    num1=input("What is the UPC number you'd like to check?\n\n")

    # converts the number to a list
    num2=list(num1)

    # reverses the list
    num3=(num2[::-1])

    # numbers in odd position
    ODDpos=list(map(int,num3[1::2]))

    # numbers in even position as integers
    EVENpos=list(map(int,num3[0::2]))

    # Tests if the length is greater than 2
    if (len(num3) <= 2):
        print("Please enter a valid UPC")
        return False

    # Tests if the string only consists of 0s
    elif sum(list(map(int, num3)))==0:
        print("Please enter a valid UPC")
        return False


    # Continue with function to perform UPC check
    else: 
        for i in ODDpos:

            # this is multiplying all the odd elements by 3 instead of elements in an odd spot
            numODD = i * 3

            # adds the newly multiplied elements into the set 'ODDSby3'
            ODDSby3.append(numODD)

        # adds the newly multiplied elements in 'ODDSby3' to even position numbers in EVENpos
        Final = ODDSby3 + EVENpos

        S = sum(Final)
        if S % 10 == 0:
            print("True")
            return True
        else:
            print("False")
            return False

is_valid_upc()
