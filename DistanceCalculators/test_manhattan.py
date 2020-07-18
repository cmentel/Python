"""
Connor Mentel
CS 5001
HW 2
Programming #3
Testing your Functions - Manhattan
"""

from distance2 import absolute
from distance2 import manhattan2

EPSILON = .0001

def test_manhattan():
    ''' function test_absolute
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on the manhattan distance
              function, makes sure each value
              is as-expected.
    '''
        
    num_failed = 0

    # Test 1: (0, 0), (0, 0)
    # Distance should be 0
    actual = manhattan2(0, 0, 0, 0)
    expected = 0.0
    print('Input (0, 0), (0, 0).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    
    
    # Test 2: (2, -1), (-2, 2).
    # Distance is 7
    actual = manhattan2(2, -1 ,-2, 2)
    expected = 7
    print('Input (2, -1), (-2, 2).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1


    # Test 3: (1, 1), (0, 1)
    # Distance is 1.0
    actual = manhattan2(1, 1, 0, 1)
    expected = 1
    print('Input (1, 1), (0, 1).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1


    # Test 4: (-5.2, 3.8), (-13.4, 0.2)
    # Distance is 11.8
    actual = manhattan2(-5.2, 3.8, -13.4, 0.2)
    expected = 11.8
    print('Input (-5.2, 3.8), (-13.4, 0.2).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    return num_failed
    
def main():
    num_fail = test_manhattan()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.')

main()
    