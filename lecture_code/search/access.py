from cmput274 import *
from time import time
@TCO
def getIthHelper(l, i):
  if i == 0:
    return first(l)
  return getIthHelper(rest(l), i-1)

def getIth(l, i):
  return trampoline(getIthHelper(l, i))


def timeLLIth(l, i, n):
  '''
  run getIth(l, i) n times
      and return the time it took
  '''
  if n == 0:
    return
  curTime = time()
  val = getIth(l, i)
  timeLLIth(l, i, n-1)
  newTime = time()
  return newTime - curTime

def timeTupleIth(t, i, n):
  if n == 0:
    return
  curTime = time()
  val = t[i]
  timeTupleIth(t, i, n-1)
  newTime = time()
  return newTime - curTime
