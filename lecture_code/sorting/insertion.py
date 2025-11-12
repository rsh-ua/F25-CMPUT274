from cmput274 import *

def insertionSort(l):
  '''
  Returns the sorted in non-descending version of
  the LList l
  '''
  def insert(v, sl):
    '''
    Insert the value v into the sorted
    LList sl
    '''
    if isEmpty(sl) or v < first(sl):
      return cons(v, sl)
    return cons(first(sl), insert(v, rest(sl)))
  if isEmpty(l):
    # the empty list is implicitly sorted!
    return l
  return insert(first(l), insertionSort(rest(l)))

