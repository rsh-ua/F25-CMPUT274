from cmput274 import *

def findPairsSorted(t, target):
  def helper(start, end):
    l = t[start]
    r = t[end]
    if start >= end:
      return empty()
    if l + r > target:
      return helper(start, end-1)
    if l + r < target:
      return helper(start+1, end)
    return cons(LL(l, r), helper(start+1, end-1))
  return helper(0, len(t)-1)
