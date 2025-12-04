# PRACTICE QUESTION!

def removeOccurrences(l, elem):
  '''
  removeOccurrences that removes all occurrences of the given
                    element elem in the list l by mutating it
                    and returns the number of elements removed

  l       - list of X
  elem    - X
  returns - int, number of occurrences removed

  Side effects: Mutates the list l removing all occurrences of elem

  Examples:
    removeOccurrences([1, 2, 3, 1, 4, 5, 1, 1, 6, 1, 1, 1], 1)
      -> 7
      mutates the list to be [2, 3, 4, 5, 6]
  '''
  count = 0
  i = 0
  while i < len(l):
    if l[i] == elem:
      count = count + 1
      l.pop(i)
    else:
      i = i + 1
  return count
