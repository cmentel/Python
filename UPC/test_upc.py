'''
CS5001
Testing code for HW4 -- UPC validation
'''

from upc import is_valid_upc


def test_valid_upc():
    ''' Function test_valid_upc
        Input: Nothing
        Returns: int, number of tests that failed.
        Does: Invokes the is_valid_upc function on several different
              inputs, expecting the function to return True. Counts the
              number of times it returns False instead, chalking them
              up as fails.
    '''
    num_failed = 0

    # Test 1: 12-digit UPC, starts with 0
    test_input = '073854008089'
    print('Testing', test_input, 'is valid...', end = '')
    if is_valid_upc(test_input):
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    # Test 2: 12-digit UPC, starts / ends w non 0
    test_input = '718103167956'
    print('Testing', test_input, 'is valid...', end = '')
    if is_valid_upc(test_input):
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    # Test 3: 13-digit UPC, starts/ends with non-zero
    test_input = '9781491939369'
    print('Testing', test_input, 'is valid...', end = '')
    if is_valid_upc(test_input):
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    # Test 4: 13-digit UPC, ends with zero
    test_input = '9781494969660'
    print('Testing', test_input, 'is valid...', end = '')
    if is_valid_upc(test_input):
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    # Test 5: 5-digit UPC, still valid
    test_input = '079900'
    print('Testing', test_input, 'is valid...', end = '')
    if is_valid_upc(test_input):
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    return num_failed

def test_invalid_upc():
    ''' Function test_invalid_upc
        Input: Nothing
        Returns: int, number of tests that failed.
        Does: Invokes the is_valid_upc function on several different
              inputs, expecting the function to return False. Counts the
              number of times it returns True instead, chalking them
              up as fails.
    '''
    num_failed = 0

    # Test 1: 12-digit UPC, mistyped a 6 as 5 from a valid one
    test_input= '718103167955'
    print('Testing', test_input, 'is not valid...', end = '')
    if not is_valid_upc(test_input):
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    return num_failed

def main():
    print('Testing VALID upc numbers.\n')
    num_fails = test_valid_upc()
    if num_fails == 0:
        print('All valid tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')

    print('Testing INVALID upc numbers.\n')
    num_fails = test_invalid_upc()
    if num_fails == 0:
        print('All invalid tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')

main()
    
        
