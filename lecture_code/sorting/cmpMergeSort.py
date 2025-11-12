from cmput274 import *

def takeN(l, n):
  '''
  Returns the first n elements of l
  '''
  if n == 0:
    return empty()
  return cons(first(l), takeN(rest(l), n-1))

def skipN(l, n):
  '''
  Returns l except for the first n elements
  '''
  if n == 0:
    return l
  return skipN(rest(l), n-1)

def mergeSort(l, cmp):
  def merge(sl1, sl2):
    # Merges two sorted lists into
    # a single sorted list
    if isEmpty(sl1):
      return sl2
    if isEmpty(sl2):
      return sl1
    if cmp(first(sl1), first(sl2)):
      return cons(first(sl1), merge(rest(sl1), sl2))
    # Otherwise first of second list is smallest element
    return cons(first(sl2), merge(sl1, rest(sl2)))
  if isEmpty(l) or isEmpty(rest(l)):
    return l # 1 or 0 element list already sorted
  fh = mergeSort(takeN(l, len(l)//2), cmp)
  sh = mergeSort(skipN(l, len(l)//2), cmp)
  return merge(fh, sh)
