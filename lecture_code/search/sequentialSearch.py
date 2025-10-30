
from cmput274 import *

def sequentialSearch(v, l):
  '''
  sequentialSearch performs sequential search on l
                   for the given value v, returns
                   True if it is found, False otherwise
  v       - any
  l       - LList of any
  returns - bool

  Examples:
    sequentialSearch(5, LL(1, 2, 5, 10, 12)) -> True
    sequentialSearch(3, LL(7, 2, 9, 8)) -> False
  '''
  if isEmpty(l):
    return False
  if first(l) == v:
    return True
  return sequentialSearch(v, rest(l))
