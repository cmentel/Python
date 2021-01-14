def get_number_of_people():
    acceptable = False
    while not acceptable:
        number_of_people = input("How many people are in the circle?\nEnter 'Q' to Quit!\n")
        if number_of_people.lower() == "q":
            return 0
        try:
            number_of_people = int(number_of_people)
            if number_of_people > 0:
                acceptable = True
                return number_of_people
            else:
                print("Please input a positive number greater than 0")
        except:
            print("Please input a positive number greater than 0")


def move_first_one_to_end(binary):
    length = len(binary)
    binary.append(binary[0])
    binary[0] = 0
    return binary


def base_ten_to_binary(number):
    binny = []
    while number != 0:
        mod = number % 2
        number = number // 2
        binny.append(mod)
        bynny = binny[::-1]
    return bynny


def binary_to_base_ten(number):
    no_leading_zeros = removeZeros(number)
    backwards = no_leading_zeros[::-1]
    holder = 0
    spot = 0
    for i in backwards:
        spot += i * (2 ** holder)
        holder += 1
    return spot


def removeZeros(a):
    no_leading_zeros = []
    n = len(a)
    ind = -1

    for i in range(n):
        if (a[i] != 0):
            ind = i
            break

    if (ind == -1):
        print("Array has leading zeros only")
        return

    b = [0] * (n - ind)

    for i in range(n - ind):
        b[i] = a[ind + i]
        no_leading_zeros.append(b[i])

    return no_leading_zeros


def get_position_to_stand(people):
    binary = base_ten_to_binary(people)
    binary = move_first_one_to_end(binary)
    position = binary_to_base_ten(binary)
    return position


def begin():
    people = get_number_of_people()
    if people == 0:
        return False
    print("There are", people, "people in the circle")
    best_spot = get_position_to_stand(people)
    print("You should stand in position", best_spot, "\n")
    return True


def keep_going():
    going = True
    while going:
        going = begin()
        if going == False:
            print("Thanks for playing!")
            break


keep_going()
