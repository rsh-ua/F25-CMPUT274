from cmput274 import *

def adderGenerator(n):
  '''
  adderGenerator returns a unary function that
                 adds n to its parameter

  n       - a Num
  returns - (Num -> Num)

  Examples:
    adderGenerator(3)(10) -> 13
    adderGenerator(5)(10) -> 15
    map(adderGenerator(2), LL(1, 2, 3)) -> LL(3, 4, 5)
  '''
  return lambda x: x + n
