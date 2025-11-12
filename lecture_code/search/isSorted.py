from cmput274 import *

def isSorted(t):
  '''
  returns true if t is sorted
          in either non-decreasing
          or non-increasing order
  '''
  def isNonDecreasing(i):
    # non decreasing means
    # for each i, t[i] <= t[i+1]
    if i >= len(t):
      # This in effect is the
      # empty tuple, so true
      return True
    if i == len(t) - 1:
      # this in effect is the
      # tuple with ONE element
      # so also true
      return True
    # if not a base case
    # we must check if t[i] <= t[i+1]
    return t[i] <= t[i+1] and isNonDecreasing(i+1)
  def isNonIncreasing(i):
    if i >= len(t):
      return True
    if i == len(t)-1:
      return True
    return t[i] >= t[i+1] and isNonIncreasing(i+1)
  return isNonDecreasing(0) or isNonIncreasing(0)

# But, the above two helper functions
# isNonIncreasin and isNonDecreasing
# have exactly the same code EXCEPT for
# the comparison of the two elements itself.
# Can we abstract that away?


def isOrdered(comp, t):
  '''
  isOrdered takes a binary comparator function
            comp and a tuple t and returns true
            if t is ordered relative to comp.

  comp    - (X X -> bool)
  t       - tuple of X
  returns - bool
  '''
  def isOrderedHelper(i):
    if i >= len(t)-1:
      # Tuple of len 1 or 0 is always ordered
      return True
    return comp(t[i], t[i+1]) and isOrderedHelper(i+1)
  return isOrderedHelper(0)

def isSorted2(t):
  return isOrdered(lambda x, y: x <= y, t) or isOrdered(lambda x, y: x >= y, t)
