from cmput274 import *
def skipGen(n):
  '''
  skipGen returns the function f such that when f is applied to
          a LList it returns a new LList the result of skipping
          every nth element of the LList

  n - a natural number > 1
  returns - (LList -> LList)

  Examples:
    skipGen(3)(LL(10,22,36,47,59,60,72,80))
          -> (10, 22, 47, 59, 72, 80)
    skipGen(2)(LL("a","b","c","d"))
          -> ("a", "c")
  '''
  def skipHelper(l, i):
    if isEmpty(l):
      return empty()
    if i%n == 0:
      return skipHelper(rest(l), i+1)
    return cons(first(l), skipHelper(rest(l), i+1))

  return lambda l: skipHelper(l, 1)
