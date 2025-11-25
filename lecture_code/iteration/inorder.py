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



pop = rest
push = cons
peek = first


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
  # To solve this problem we will build our own
  # stack to simulate that done implicitly by
  # recursion. We'll implement a stack using
  # a LList
  stack = LL(t)
  # Our stack will be a stack of trees
  # and the first tree will always be
  # the tree to process next.
  answer = empty()
  # answer is going to be our answer so far
  # that we build up as we go along
  while not isEmpty(stack):
    cur = peek(stack)
    stack = pop(stack)
    if not isEmpty(second(cur)):
      # Place current back on top of the stack but without
      # a left subtree
      stack = push(LL(first(cur), empty(), third(cur)), stack)
      # Push our left tree onto the stack so that it may
      # be processed next.
      stack = push(second(cur), stack)
    elif first(cur) != None: # Have I processed this node's data yet?
      data = first(cur)
      # To process this place it in my answer so far
      answer = cons(data, answer)
      stack = push(LL(None, second(cur), third(cur)), stack)
    elif not isEmpty(third(cur)):
      # Push current back on top of the stack but without
      # a right subtree (since it'll already be processed
      # by the time we reach this node again on the stack)
      stack = push(LL(first(cur), second(cur), empty()), stack)
      # Push our right subtree onto the stack for processing
      stack = push(third(cur), stack)
  return foldl(answer, cons, empty())


def inBTreeToLList2(t):
  stack = LL(t)
  answer = empty()
  while not isEmpty(stack):
    cur = peek(stack)
    stack = pop(stack)
    if not isEmpty(second(cur)):
      # Place current back on top of the stack but without
      # a left subtree
      stack = push(LL(first(cur), empty(), third(cur)), stack)
      # Push our left tree onto the stack so that it may
      # be processed next.
      stack = push(second(cur), stack)
    else:
      # If I don't have a left subchild then simply
      # process the current node and then push the
      # right subchild for processing
      answer = cons(first(cur), answer)
      if not isEmpty(third(cur)):
        stack = push(third(cur), stack)
  return foldl(answer, cons, empty())
