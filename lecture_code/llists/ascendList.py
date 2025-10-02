from cmput274 import *

def append(elem, l):
  if isEmpty(l):
    return cons(elem, l)
  return cons(first(l), append(elem, rest(l)))


def ascendList(n):
  if n == 0:
    return cons(0, empty())
  return append(n, ascendList(n-1))
