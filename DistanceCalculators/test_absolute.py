"""
Connor Mentel
CS 5001
HW 2
Programming #3
Testing your Functions - Absolute
"""

distance2 = __import__("distance2")

EPSILON = .0001


def test_absolute():
    ''' function test_absolute
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on the absolute
              function, makes sure each value
              is as-expected.
    '''

    num_failed = 0

    # Test 1: (-4)
    # Value should be 4
    actual = distance2.absolute(-4)
    expected = 4
    print('Input (-4).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if distance2.absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1

    # Test 2: (0).
    # Value should be 0
    actual = distance2.absolute(0)
    expected = 0
    print('Input (2, -1), (-2, 2).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if distance2.absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1

    # Test 3: (3)
    # Value should be 1
    actual = distance2.absolute(3)
    expected = 3
    print('Input (1, 1), (0, 1).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if distance2.absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1

    # Test 4: (-5.2)
    # Value should be 5.2
    actual = distance2.absolute(-5.2)
    expected = 5.2
    print('Input (-5.2, 3.8), (-13.4, 0.2).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if distance2.absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    return num_failed


def main():
    num_fail = test_absolute()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.')


main()
