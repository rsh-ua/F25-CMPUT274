from cmput274 import *

def sumList(l):
  '''
  Sums all the integers in a LList of integers
       using a while loop
  '''
  sum = 0
  while not isEmpty(l):
    sum = sum + first(l)
    l = rest(l)
  return sum

