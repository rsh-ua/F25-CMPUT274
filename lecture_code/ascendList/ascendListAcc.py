from cmput274 import *
import sys

@TCO
def ascendListAcc(n, acc):
  if n == 0:
    return cons(0, acc)
  return ascendListAcc(n-1, cons(n, acc))


def ascendList(n):
  return ascendListAcc(n, empty())


if __name__ == "__main__":
  n = int(sys.argv[1])
  print(ascendList(n))
