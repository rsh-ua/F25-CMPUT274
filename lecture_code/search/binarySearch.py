

def bsContains(v, t):
  '''
  bsContains performs binary search on the tuple t
             to find if the element v is contained
             within it or not.

  v       - any
  t       - tuple of any sorted in non-decreasing order
  returns - bool

  Examples:
    bsContains(5, (1, 2, 3, 4 5)) -> True
    bsContains(3, (6, 8, 10, 11)) -> False
  '''
  def bsHelper(start, end):
    '''
    start - Nat, first index in the slice
            of the tuple that is relevant
    end   - Nat, last index that is
            in the tuple that is relevant
    e.g.
      start = 4, end = 10
      then we care about the tuple indices
      from [4, 10]
    '''
    midpoint = (end-start)//2 + start
    if start > end:
      return False
    if t[midpoint] == v:
      return True
    if t[midpoint] > v:
      return bsHelper(start, midpoint-1)
    if t[midpoint] < v:
      return bsHelper(midpoint+1, end)
  return bsHelper(0, len(t)-1)
