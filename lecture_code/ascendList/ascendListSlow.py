from cmput274 import *
import sys
sys.setrecursionlimit(10000000)
def append(elem, l):
  if isEmpty(l):
    return cons(elem, empty())
  return cons(first(l), append(elem, rest(l)))


def ascendListCPS(n, thunk):
  if n == 0:
    return cons(0, empty())
  return 

def ascendList(n):
  if n == 0:
    return append(0, empty())
  return append(n, ascendList(n-1))



def main():
  n = int(sys.argv[1])
  print(ascendList(n))

if __name__ == "__main__":
  main()
