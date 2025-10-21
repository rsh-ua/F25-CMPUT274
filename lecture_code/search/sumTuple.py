from cmput274 import *

@TCO
def sumTupleHelper(t, n, asf):
  if n >= len(t):
    return asf
  return sumTupleHelper(t, n+1, asf + t[n])

def sumTuple(t):
  return trampoline(sumTupleHelper(t, 0, 0))


@TCO
def sumTupleHelperSlow(t, asf):
  if len(t) == 0:
    return asf
  return sumTupleHelperSlow(t[1:], asf + t[0])

def sumTupleSlow(t):
  return trampoline(sumTupleHelperSlow(t, 0))


def timeSumTuple(f, t, n):
  '''
  timeSumTuple takes a function f which is an
               implementation of the sumTuple
               function, a tuple t, and a number
               of times to run it n and returns
               the amount of time it took to
               run f(t) n times

  '''
  from time import time
  def runNTimes(i):
    if i == 0:
      return 0
    f(t)
    runNTimes(i-1)

  startTime = time()
  runNTimes(n)
  endTime = time()
  return endTime - startTime
