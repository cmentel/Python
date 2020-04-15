"""
Connor Mentel
CS 5002 - Foundations
Programming #2
mbta_test.py
"""

from mbta import is_valid_station
from mbta import get_direction
from mbta import get_num_stops

def test_valid_mbta():
    ''' Function test_valid_mbta
        Input: Nothing
        Returns: int, number of tests that failed.
        Does: Invokes the mbta function on several different
              inputs, expecting the function to return True. Counts the
              number of times it returns False instead, chalking them
              up as fails.
    '''
    num_failed = 0
    num_tests = 0

# Test 1: Shawmut to Fields Corner. Output: 1 stop, towards Alewife
    # Test 1aa: If Shawmut is a valid station.
    test_input = ("Shawmut")
    print('Testing', test_input, 'is valid...', end='')
    if is_valid_station(test_input):
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    # Test 1ab: If Fields Corner is a valid station.
    test_input = ("Fields Corner")
    print('Testing', test_input, 'is valid...', end='')
    if is_valid_station(test_input):
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    # Test 1b: The direction train is headed [expected = Alewife]
    test_input1 = ("Shawmut")
    test_input2 = ("Fields Corner")
    print('Testing', test_input1, "to", test_input2, "headed to Alewife ", end='')
    if get_direction(test_input1,test_input2):
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    # Test 1c: The number of stops [expected value = 1]
    test_input1 = ("Shawmut")
    test_input2 = ("Fields Corner")
    print('Testing number of stops from', test_input1, "to", test_input2, "'is valid...'", end='')
    if get_num_stops(test_input1,test_input2) == 1: #1 stop expected
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

# Test 2: Ashmont to Alewife. Output: 16 stops, towards Alewife.
    # Test 2aa: If Ashmont is a valid station.
    test_input = ("Ashmont")
    print('Testing', test_input, 'is valid...', end='')
    if is_valid_station(test_input):
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    # Test 2ab: If Alewife is a valid station.
    test_input = ("Alewife")
    print('Testing', test_input, 'is valid...', end='')
    if is_valid_station(test_input):
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    # Test 2b: The direction train is headed [expected = Alewife]
    test_input1 = ("Ashmont")
    test_input2 = ("Alewife")
    print('Testing', test_input1, "to", test_input2, "headed to Alewife ", end='')
    if get_direction(test_input1,test_input2) == "Alewife":
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_failed += 1
        num_tests = num_tests + 1

    # Test 2c: The number of stops [expected value = 16]
    test_input1 = ("Ashmont")
    test_input2 = ("Alewife")
    print('Testing number of stops from', test_input1, "to", test_input2, "'is valid...'", end='')
    if get_num_stops(test_input1,test_input2) == 16: #1 stop expected
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

# Test 3: Kendall to Savin Hill. Output: 8 stops, towards Ashmont.
    # Test 3aa: If Kendall is a valid station
    test_input = ("Kendall")
    print('Testing', test_input, 'is valid...', end='')
    if is_valid_station(test_input):
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    # Test 3ab: If Savin Hill is a valid station
    test_input = ("Savin Hill")
    print('Testing', test_input, 'is valid...', end='')
    if is_valid_station(test_input):
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    # Test 3b: The direction train is headed [expected = Ashmont]
    test_input1 = ("Kendall")
    test_input2 = ("Savin Hill")
    print('Testing', test_input1, "to", test_input2, "headed to Ashmont ", end='')
    if get_direction(test_input1,test_input2) == "Ashmont":
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    # Test 3c: The number of stops [expected value = 8]
    test_input1 = ("Kendall")
    test_input2 = ("Savin Hill")
    print('Testing number of stops from', test_input1, "to", test_input2, "'is valid...'", end='')
    if get_num_stops(test_input1,test_input2) == 8: # stop expected
        print('SUCCESS!\n')
        num_tests = num_tests + 1
    else:
        print('FAIL :(\n')
        num_tests = num_tests + 1
        num_failed += 1

    return num_failed
    return num_tests


def main():
    print('Testing VALID MBTA.\n')
    num_fails = test_valid_mbta()
    num_tests = test_valid_mbta()

    if num_fails == 0:
        print('\nAll 12 tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')


main()




