from cmput274 import *

def sumList1(l):
  return foldl(l, lambda x, y: x + y, 0)


def sumList2(l):
  sum = 0
  for i in l:
    sum = sum + i
  return sum
