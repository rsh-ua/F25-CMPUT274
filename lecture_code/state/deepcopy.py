

# Hint: Remember the type function that can return the type
#       of a piece of data, and remember that you can compare
#       that with the name of a type
#       i.e. before we did type(x) == LList
#       since this type is list you could do
#       type(x) == l

def deepcopy(l):
  '''
  deepcopy returns a DEEPCOPY of the list l

  l       - list of any
  returns - list of any

  Side effects: None

  Examples:
    deepcopy([[1, 2], [3, 4]])
      -> [[1, 2], [3, 4]] BUT ALL ALIASING IS BROKEN!
  '''
