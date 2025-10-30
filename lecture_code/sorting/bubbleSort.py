from cmput274 import *

def second(l):
  return first(rest(l))

def pluckSecond(l):
  # Removes the second element of l
  # Assumes a list of atleast length 2
  return cons(first(l), rest(rest(l)))

def bubbleSort(l):
  '''
  Returns a sorted list of L in
  non-decreasing order by applying
  bubblesort to it.
  '''
  def bubble(l):
    '''
    One "bubbling" of the list
    '''
    if isEmpty(l) or isEmpty(rest(l)):
      # if len(l) <= 1 no more pairs
      # Can't bubble!
      return l
    if first(l) > second(l):
      # swap!
      return cons(second(l), bubble(pluckSecond(l)))
    # Otherwise, don't swap
    return cons(first(l), bubble(rest(l)))

  def repeatBubble(l, n):
    # Bubbles n times
    if n == 0:
      return l
    return repeatBubble(bubble(l), n-1)
  return repeatBubble(l, len(l))
