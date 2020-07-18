'''
Connor Mentel
CS 5001 - HW 5
Programming #1
Due: Thursday October 31
'''

# imports
HanoiViz = __import__("hanoi_viz")



# list of acceptable inputs
DISK_RANGE = [2,3,4,5,6,7,8]


# assigning names of the towers
source = "A" #source
target = "C" #target
middle = "B" #aux


# moves the disks and calls itself and move disk function
def move_tower(disks,source,target,middle,towers):
    if disks >=1:
        move_tower(disks-1, source, middle, target, towers)
        HanoiViz.move_disk (source, target, towers)
        move_tower(disks-1, middle, target, source, towers)
    else:
        return


# main function calling others
def main():

    # asks for the number of disks
    disks = int(input("What is the number of disks? (2-8)\n"))

    # validates that disks is an integer and not a float, and that input is in range 2-8
    if disks not in DISK_RANGE:
        print("Oops that's not a number or isn't in the permissible range"
              ", please try again!")
        main()

    else:
        # converts input to integer
        num_disks = int(disks)
        towers = HanoiViz.initialize_towers(num_disks, source, middle, target)
        move_tower(disks,source,middle,target,towers)


main()