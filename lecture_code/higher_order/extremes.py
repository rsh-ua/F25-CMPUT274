from cmput274 import *

def exComb(n, pair):
  '''
  exComb takes an int n, and pair of
         the form (MIN,MAX)
         and returns a newpair of the
         form (MIN,MAX) updating the
         MIN or MAX value respectively
         if n<MIN or n>MAX

  n - integer
  pair - LList of two integers
  return - LList of two intgers

  Examples:
    exComb(5, (10, 12)) -> (5, 12)
    exComb(6, (3, 10)) -> (3, 10)
    exComb(200, (-1, 5)) -> (-1, 200)
  '''
  if n < first(pair):
    return cons(n, rest(pair))
  if n > first(rest(pair)):
    return LL(first(pair), n)
  return pair

def extremes(l):
  return foldl(l, exComb, LL(first(l),first(l)))
