def flatten(l):
  '''
  returns a flattened version of the list l
  which may contain lists (but for now not tuples or llists)
  '''

  return foldr(l, lambda elem, result: (flatten(elem) if type(elem) == list else 
                [elem]) + result, [])


def flatten(l):
  newL = []
  for item in l:
    if type(item) == list:
      newL = newL + flatten(item)
    else:
      newL.append(item)
  return newL
