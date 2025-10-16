from cmput274 import *
from ascendListAcc import ascendList
from map import *
def buildList(f, n):
  '''
  buildList produces a LList generated
            from the function f, where
            f is mapped onto the values
            from 0 to n-1

  f       - (Nat -> X)
  n       - Nat
  returns - LList of X

  Examples:
    def pow2(x):
      return 2**x

    buildList(pow2, 5) -> (1, 2, 4, 8, 16)

    def double(x):
      return 2*x
    buildList(double, 7) -> (0, 2, 4, 6, 8, 10, 12)
  '''
  return map(f, ascendList(n-1))
