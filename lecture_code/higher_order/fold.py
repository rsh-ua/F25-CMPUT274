from cmput274 import *
def fold(l, combine, base):
  '''
  fold folds the function combine over the LList l with the
       base value acting as our final second operand.

  l       - LList
  combine - (X Y -> Y)
  base    - Y
  returns - Y
  '''
  if isEmpty(l):
    return base
  return combine(first(l), fold(rest(l), combine, base))
