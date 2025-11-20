from cmput274 import *

'''
A BTree of X is one of:
- empty()
- LList(X, BTree of X, BTree of X)
e.g.
            5
          /  \
         3    10
        / \     \
       2   7     11
Would be represented by

LL(5,
   LL(3,
     LL(2, empty(), empty()),
     LL(7, empty(), empty())),
   LL(10,
      empty(),
      LL(11, empty(), empty())))
'''

tExample = LL(5,
              LL(3,
                 LL(2, empty(), empty()),
                 LL(7, empty(), empty())),
              LL(10,
                 empty(),
                 LL(11, empty(), empty())))

# Write a function isLeaf which takes a BTree and returns True
# if the node given is a leaf node.
def isLeaf(t):
  '''
  Takes a BTree T and returns true
  if the node T is a leaf node.

  A node is a leaf node if it has no children.
  A node has no children if its left child and
  right child are empty
  '''
  if isEmpty(t):
    return False
  return second(t) == empty() and third(t) == empty()


def concatenate(l1, l2):
  '''
  returns the result of concatenating
  l1 and l2
  '''
  return foldr(l1, cons, l2)


'''
Write inBTreeToLList using only iteration
you may not use any recursive functions
you may not use any higher order functions
'''
def inBTreeToLList(t):
  '''
  inBTreeToLList produces a LList which is the result
                   of walking the tree T in post order

  t - BTree of X
  returns - a LList of X

  Examples:
    t =LL(5,
          LL(3,
             LL(2, empty(), empty()),
             LL(7, empty(), empty())),
          LL(10,
             empty(),
             LL(11, empty(), empty())))
    inBTreeToLList(t) -> (2, 3, 7, 5, 10, 11)
  '''
