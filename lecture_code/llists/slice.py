from cmput274 import *


def slice(l, start, end):
  '''
  slice returns a new LList that is
        the values in the range [start,end)
        from the LList l

  returns - LList
  l       - LList
  start   - natural number start >= 0, start < length(l)
  end     - natural number end >= start, end <= length(l)
  '''
  if end == 0:
    return empty()
  if start > 0:
    return slice(rest(l), start-1, end-1)
  return cons(first(l), slice(rest(l), start, end-1))
