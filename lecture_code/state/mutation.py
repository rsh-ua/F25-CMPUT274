

def foo(x):
  '''
  foo takes a list of integers and
      mutates the first one to be
      double what it is

  x       - list of int
  returns - None

  Side Effects: mutates the given list parameter
                such that the first item is doubled

  Examples:
    l = [10]
    foo(x) -> None and modifies l to be [20]
  '''
  x[0] = x[0]*2


def blah(y):
  s = [y]
  foo(s)
  return s[0]
