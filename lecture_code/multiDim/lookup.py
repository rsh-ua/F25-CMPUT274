
from cmput274 import *

'''
A Dictionary is a LList of LL(X, Y)
'''

second = lambda l: first(rest(l))

def lookup(key, dct):
  '''
  lookup takes a key and a Dictionary
         returns the value that corresponds
         to the key in the dictionary if it
         exists, "" otherwise
  '''
  if isEmpty(dct):
    return ""
  # The first of my dictionary is a pair
  # of the form (key, val)
  # If the key is the one I'm looking for
  # I should return the matching value
  if first(first(dct)) == key:
    return second(first(dct))
  return lookup(key, rest(dct))
