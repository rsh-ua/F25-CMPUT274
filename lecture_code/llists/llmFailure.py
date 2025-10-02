'''
(define (ascendList n)
  (if (= n 0)
      (cons 0 empty)
      (cons (- n 1) (ascendList (- n 1))))
'''

from cmput274 import *

def ascendList(n):
  if n == 0:
    return cons(0, empty())
  return cons(n - 1, ascendList(n - 1))
