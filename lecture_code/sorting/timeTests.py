from time import time

def timeSort(sort, l, n):
  def runN(n):
    if n == 0:
      return
    sl = sort(l)
    return runN(n-1)
  start = time()
  runN(n)
  end = time()
  return end-start
