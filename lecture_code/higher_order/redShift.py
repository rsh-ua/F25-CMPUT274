from cmput274 import *


'''
A CV is:
  - an int in range [0,255]

A Pixel is a:
- LL(CV, CV, CV)
'''

def redShiftHelper(p, sAmt):
  newRed = first(p) + sAmt
  if newRed > 255:
    return cons(255, rest(p))
  return cons(newRed, rest(p))



def redShift(sAmt):
  '''
  redShift returns a function that takes one pixel
           parameter and returns the result of shifting
           its red value by sAmt

  sAmt - Natural
  returns - (Pixel -> Pixel)

  Examples:
    redShift(5)(LL(20, 30, 5)) -> (25, 30, 5)
    redShift(100)(LL(20, 30, 5)) -> (120, 30, 5)
  '''
  return lambda p: redShiftHelper(p, sAmt)
