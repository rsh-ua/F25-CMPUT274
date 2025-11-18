from cmput274 import

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
  if type(sl)
