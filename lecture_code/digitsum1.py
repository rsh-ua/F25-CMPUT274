from logfloor import *
from cmput274 import *

def digitSum(n):
  if n < 10:
    return n
  # Pluck out the left most digit
  digit = n//(10**logFloor(n))
  # Now digit is the MSD of n.
  # n - digit*10**logFloor(n) removes
  # the most significant digit from n
  return digit + digitSum(n - digit*10**logFloor(n))
