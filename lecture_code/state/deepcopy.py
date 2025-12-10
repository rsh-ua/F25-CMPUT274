

# Hint: Remember the type function that can return the type
#       of a piece of data, and remember that you can compare
#       that with the name of a type
#       i.e. before we did type(x) == LList
#       since this type is list you could do
#       type(x) == l

def deepcopy(l):
  '''
  deepcopy returns a DEEPCOPY of the list l

  l       - X
  returns - X

  Side effects: None

  Examples:
    deepcopy([[1, 2], [3, 4]])
      -> [[1, 2], [3, 4]] BUT ALL ALIASING IS BROKEN!
  '''
  if type(l) != list:
    return l
  newL = []
  for item in l:
    newL.append(deepcopy(item))
  return newL


def naiveDeepCopy(l):
  # Only deep copies the first depth level
  # if there are mutable data types deeper
  # than the first level it won't deepcopy them
  newL= []
  for item in l:
    if type(item) == list:
      newL.append(item.copy())
    else:
      newL.append(item)
  return newL
