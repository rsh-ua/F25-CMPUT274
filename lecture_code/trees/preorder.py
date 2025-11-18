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
     LL(2, empty(), empty())
     LL(7, empty(), empty())),
   LL(10,
      empty(),
      LL(11, empty(), empty())))
'''

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
  return first(rest(t)) == empty() and first(rest(rest(t))) == empty()


def preBTreeToLList(t):
  '''
  preBTreeToLList performs a preorder traversal of t
                  and builds a LList from the values
                  of t

  t - BTree of Any
  returns - LList of Any

  Examples:
    t = LL(5,
          LL(3,
             LL(2, empty(), empty())
             LL(7, empty(), empty())),
          LL(10,
             empty(),
             LL(11, empty(), empty())))

  preBTreeToList(t) -> LL(5, 3, 2, 7, 10, 11)
  '''
  
