from cmput274 import *
def count1(c, n):
  '''
  count1 c n returns n+1 if c == "1"
         or n otherwise

  c       - character
  n       - an integer
  returns - an integer

  Example:
    count1("1", 5) -> 6
    count1("0", 7) -> 7
  '''
  if c == "1":
    return 1 + n
  return n

def parity(s):
  return   foldr(s, count1, 0) % 2 == 0


def checkOne(c, b):
  '''
  checkOne checks if c is a one or not
           if it is returns the negation
           of b, otherwise returns b

  c - char
  b - bool
  returns - bool

  Examples:
    checkOne("1", False) -> True
    checkOne("1", True) -> False
    checkOne("0", False) -> False
  '''
  if c == "1":
    return not b
  return b
def parity2(s):
  return foldr(s, checkOne, True)
