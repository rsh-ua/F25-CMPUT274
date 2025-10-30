from cmput274 import *


def findPairs(t, target):
  '''
  Returns the LList of pairs of
  integers from tuple t that sum
  to target
  '''
  def findPairHelper(first, cur):
    if first >= len(t) - 1:
      return empty()
    ror = (findPairHelper(first, cur+1) if cur < len(t)-1 else
            findPairHelper(first+1, first+2))

    if t[first] + t[cur] == target:
      return cons(LL(t[first], t[cur]), ror)
    return ror
  return findPairHelper(0, 1)


def findPairs2(t, target):
  def checkForPairs(i):
    '''
    returns pairs that sum with index i
            to target from t
    '''
    def checkNext(j):
      if j >= len(t):
        return empty()
      if t[i] + t[j] == target:
        return cons(LL(t[i], t[j]), checkNext(j+1))
      return checkNext(j+1)

    if i >= len(t)-1:
      return empty()
    return foldr(checkNext(i+1), cons, checkForPairs(i+1))
  return checkForPairs(0)
