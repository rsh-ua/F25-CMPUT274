from cmput274 import *

def filter(p, l):
  '''
  filter filters the LList l with the
         given predicate p such that
         elements appear in the resultant
         list if and only if p(e) -> True

  returns - LList of X
  p       - (X -> bool)
  l       - LList of X

  Examples:
    def isNegative(x):
      return x < 0
    def isShort(s):
      return len(s) < 5

    filter(isNegative, LL(-10, 5, -2, 0)) -> (-10, -2)
    filter(isShort, LL("abc", "zaboomafoo", "wow!", "CMPUT274", "a")) -> ("abc", "wow!", "a")
  '''
  if isEmpty(l):
    return empty()
  ror = filter(p, rest(l))
  if p(first(l)):
    return cons(first(l), ror)
  return ror
