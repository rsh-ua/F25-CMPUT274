from cmput274 import *


def map(f, l):
  '''
  map maps a function onto a LList
      and produces the result of that
      mapping

  f       - (X -> Y)
  l       - LList of X
  returns - LList of Y

  Examples:
    def add3(x):
      return x + 3

    map(add3, LL(1, 2, 3)) -> (4, 5, 6)
    map(len, LL("123", "abc", "hello")) -> (3, 3, 5)
  '''
  if isEmpty(l):
    return empty()
  ror = map(f, rest(l))
  return cons(f(first(l)), ror)


