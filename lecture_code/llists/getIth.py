from cmput274 import *

def getIth(l, i):
  '''
  getIth returns the ith element of a LList

  l       - a non-empty LList with at least i+1 items
  i       - a natural number
  returns - any, an item of the LList

  Examples:
    myL = cons(5, cons(10, cons(27, empty())))
    getIth(myL, 0) -> 5
    getIth(myL, 1) -> 10
    getIth(myL, 2) -> 27
  '''
  if i == 0:
    return first(l)
  # In order to recurse to get the ith element
  # we must decrement i to say we're look for
  # 1 element sooner.
  # However, the ith element of this list
  # is equavalent to saying the i-1th element
  # of the rest of this list
  ror = getIth(rest(l), i-1)
  # In this case, the result of our recursion IS
  # our final answer, so no additional work
  # needs to be done
  return ror
