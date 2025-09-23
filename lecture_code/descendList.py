from cmput274 import *
# This is the water
# this is the well
# Drink deep, and descend

def descendList(n):
  '''
  descendList produces an LList which stores the
              naturals n to 0 in descending order

  n       - a natural
  returns - a LList

  examples:
    descendList(5) -> (5, 4, 3, 2, 1, 0)
    descendList(2) -> (2, 1, 0)
  '''
  if n == 0:
    return cons(0, empty())
  # Assume the recursion works
  # therefore result of recursion (ror)
  # is the LList from n-1 to 0.
  ror = descendList(n-1)
  # If I already the LList from n-1
  # 0, how do I CONSTRUCT the list
  # from n to 0?
  return cons(n, ror)
