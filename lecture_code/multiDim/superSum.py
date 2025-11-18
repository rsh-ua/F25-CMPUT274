from cmput274 import *

'''
SuperList of X is one of:
- empty()
- cons(X, SuperList)
- cons(SuperList, SuperList)

This is a recursive data definition that defines a data
type that is a LList that contains elements that are either
ints, or LLists (those LLists themselves are these data types
so they have the same restrictions)

LL(1, 2, LL(4, LL(3), 7), LL(5, LL(1, 2, 3)), LL(LL(LL(5))))

Is a valid SuperList
'''


def superSum(sl):
  '''
  superSum returns the sum of ALL integers in the SuperList sl
           even if those integers are contained within SuperLists
           contained within sl

  sl - SuperList of ints
  returns - an int

  Example:
    superSum(LL(1, 2, LL(4, LL(3), 7), LL(5, LL(1, 2, 3)), LL(LL(LL(5)))))
          -> 33
  '''
  if isEmpty(sl):
    return 0
  if type(first(sl)) == int:
    # Just an int, add it to our recursive result
    return first(sl) + superSum(rest(sl))
  if type(first(sl)) == LList:
    # If the first(sl) is a SuperList then we need
    # the sum of all ints inside of it... well we have
    # the function that does that --- this one!
    return superSum(first(sl)) + superSum(rest(sl))

def superSum2(sl):
  return foldr(sl,
              lambda elem, ror: elem + ror if type(elem) == int else \
                                                 superSum2(elem) + ror
              , 0)
