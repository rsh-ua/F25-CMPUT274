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



pop = rest
push = cons
peek = first


'''
Write inBTreeToLList using only iteration
you may not use any recursive functions
you may not use any higher order functions
'''
def postBTreeToLList(t):
  stack = LL(t)
  answer = empty()
  while not isEmpty(stack):
    # each iteration of the loop is effectively a
    # "recursive call" to the fn postBTreeToLList
    # (or it is returning to an existing call)
    tree = peek(stack) # tree is of the form LL(int, tree, tree)
    stack = pop(stack)
    if not isEmpty(second(tree)):
      stack = push(LL(first(tree), empty(), third(tree)), stack)
      stack = push(second(tree), stack)
    elif not isEmpty(third(tree)):
      stack = push(LL(first(tree), empty(), empty()), stack)
      stack = push(third(tree), stack)
    else:
      # If this item has no left child and no right child
      # then I am ready to process /this/ node,
      # so simply append it to the back of my LList
      append = lambda elem, l: foldr(l, cons, LL(elem))
      answer = append(first(tree), answer)
  return answer

