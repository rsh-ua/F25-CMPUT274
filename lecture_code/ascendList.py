from cmput274 import *

def ascendListHelper(n, i):
  '''
  ascendListHelper returns the list that will have
                   n+1 elements, starting at i
                   and ascending by 1 each time

  returns - A LList
  n       - A natural number
  i       - A natural number

  Examples
    ascendListHelper(5, 0) -> (0, 1, 2, 3, 4, 5)
    ascendListHelper(2, 3) -> (3, 4, 5)
    ascendListHelper(0, 7) -> (7)
  '''
  if n == 0:
    return cons(i, empty())
  return cons(i, ascendListHelper(n-1, i+1))


def ascendList(n):
  '''
  ascendList returns a LList of the values from
             0 to n in ascending order

  returns - A LList
  n       - a natural number

  Examples:
    ascendList(5) -> (0, 1, 2, 3, 4)
    ascendList(2) -> (1, 1, 2)
  '''
  return ascendListHelper(n, 0)
