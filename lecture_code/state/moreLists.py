def main():
  l = []
  # Lists have several functions that operate on them
  # but these functions are functions defined within
  # the type list itself.
  # Such functions are called //methods//
  # and they are only different from functions
  # we've defined so far in that they are called
  # different, and take an implicit parameter

  # The list function append takes a single
  # parameter which is the value to add to the back
  # of a list, and it mutates the given list
  # such that it is one element larger, that element
  # is the one you gave, it returns None
  l.append(5) # returns None! Don't assign l to this result
  # i.e. don't say:
  # l = l.append(5)
  # the calling of the function is all you want because it
  # /mutates/ your list l doesn't create and return a new list

  # Some notes on this syntax, what does
  # l.append(5) mean?

  # Well . is the member access operator again
  # and so we are accessing the member append of
  # our list l, so that is a function.
  # But this is also the way in which we call
  # /methods/
  # Really, what append is is a function of the form
  # append(l, elem)
  # and it mutates the list l by appendin the elem
  # But instead of calling it append(l, elem)
  # we call it
  # l.append(elem)

  '''
  Another function for lists is pop
  pop takes 0 or 1 arguments

  If given 0 arguments pop targets the
  last element of the list
  if given an argument it should be a valid index
  of that list

  pop mutates the list by removing the targeted element
  and returning the element removed
  '''
  l = ["a","b","c"]
  print(f"l.pop() called on {l}")
  elem = l.pop() # removes last element and returns it
  print(l) # mutated to ["a", "b"]
  print(elem) # is "c"
  l = ["a", "b", "c", "d"]
  print(f"l.pop(1) called on {l}")
  elem = l.pop(1)
  print(l) # mutated to ["a", "c", "d"]
  print(elem) # "b"

if __name__ == "__main__":
  main()
