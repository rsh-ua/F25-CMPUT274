from cmput274 import *

def ascendListAcc(n, acc):
  if n == 0:
    return cons(0, acc)
  return ascendListAcc(n-1, cons(n, acc))


def ascendList(n):
  return ascendListAcc(n, empty())
