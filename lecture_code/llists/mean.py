from cmput274 import *

def sum(lon):
  '''
  Returns the sum of the numbers in a list of numbers
  ...
  '''
  if isEmpty(lon):
    return 0
  return first(lon) + sum(rest(lon))

def length(lon):
  if isEmpty(lon):
    return 0
  return 1 + length(rest(lon))

def mean(lon):
  '''
  mean - produces the mean of the numbers
         in lon

  lon     - a non-empty list of numbers
  returns - a float

  Examples:
    mean(cons(4.7, cons(20, cons(3, empty()))) -> 9.23333
  '''

  return sum(lon)/length(lon)
