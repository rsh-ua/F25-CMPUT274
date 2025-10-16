from cmput274 import *
def redShiftHelper(p, sAmt):
  newRed = first(p) + sAmt
  if newRed > 255:
    return cons(255, rest(p))
  return cons(newRed, rest(p))


def redShift(sAmt):
  return lambda p: redShiftHelper(p, sAmt)
