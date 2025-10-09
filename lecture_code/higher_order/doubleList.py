from cmput274 import *

def doubleList(l):
  if isEmpty(l):
    return l
  return cons(2*first(l), doubleList(rest(l)))
