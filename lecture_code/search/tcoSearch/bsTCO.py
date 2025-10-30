from cmput274 import *
@TCO
def bsHelper(v, t, start, end):
  midpoint = (end-start)//2 + start
  if start > end:
    return False
  if t[midpoint] < v:
    return bsHelper(v, t, midpoint+1, end)
  if t[midpoint] > v:
    return bsHelper(v, t, start, midpoint-1)
  return True

def bsContains(v, t):
  return trampoline(bsHelper(v, t, 0, len(t)-1))

@TCO
def seqHelper(v, t, i):
  if i >= len(t):
    return False
  if t[i] == v:
    return True
  return seqHelper(v, t, i+1)

def seqContains(v, t):
  return trampoline(seqHelper(v, t, 0))


def timeTrial(v, t, search):
  from time import time
  start = time()
  search(v, t)
  end = time()
  return end-start

def timeTrials(v, t, search, n):
  if n == 0:
    return 0
  return timeTrial(v, t, search) + timeTrials(v, t, search, n-1)


