from cmput274 import *

def purgeSortHelper(l, asf):
  # Same fn just with accum that is
  # our answer list so far.
  # Except answer so far will actually be
  # the /reverse/ of the answer so far
  # so I can always check the first item
  # as being my largest item so far
  if isEmpty(l):
    return asf
  # First check if we even /can/ take this item
  # if we wanted to
  if isEmpty(asf) or first(l) >= first(asf):
    # Then we /can/ choose to take first(l)
    # But should we?

    # The naive solution to answering the question
    # "should I take this or not"
    # is to simply NOT make a choice... do both,
    # calculating the answer if you do take
    # the item and the answer if you don't
    # and then choose whichever one is longer!
    resIfTaken = purgeSortHelper(rest(l), cons(first(l), asf))
    resNotTaken = purgeSortHelper(rest(l), asf)
    # Choose the answer that is longer...
    return resIfTaken if len(resIfTaken) > len(resNotTaken) else resNotTaken
  # if I /don't/ have a choice and I can't take this element... then don't
  return purgeSortHelper(rest(l), asf)
def purgeSort(l):
  '''
  Takes a LList and returns the optimal
  result of applying purge sort to that list
  '''

  answer = purgeSortHelper(l, empty())
  return foldl(answer, cons, empty())
