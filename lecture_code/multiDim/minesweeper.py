from cmput274 import *

'''
A MSGrid is a tuple of tuples of MSChar
'''
'''
A MSChar is one of
- "B"
- "O"
'''
def deltaGen(xDeltas, yDeltas):
  # Build a LList of all the permutations
  # of the items in xDeltas with yDeltas
  if isEmpty(xDeltas):
    return empty()
  # If xDeltas is NOT empty then
  # build every permutation of the first xDelta
  # combined with all the yDeltas
  # and combine that with our recursive result
  xd = first(xDeltas)
  # Now build a LList that contains all the pairs
  # of xd combined with the items of yDeltas
  # Except perms includes 0,0 which we do not want
  # so filter it out
  perms = filter(lambda p: first(p) != 0 or first(rest(p)) != 0,
                 map(lambda y: LL(xd, y), yDeltas))
  # So given that perms is now the permutations with this first
  # x, combine this LList with the recursive result.
  # perms is a LList of pairs
  # recursive result should be a LList of pairs
  # Combining them is concatentating
  return foldr(perms, cons, deltaGen(rest(xDeltas), yDeltas))




def adjacentBombs(grid, x, y):
  '''
  adjacentBombs returns the number of bombs
                adjacent to the cell (x,y)
                of the given grid

  grid    - a valid MSGrid
  x       - a nat
  y       - a nat
  returns - a nat

  Assumptions: x,y is within our grid

  Examples:
    g = (("B", "O", "B"), ("O", "B", "O"), ("B", "B", "B"))
    adjacentBombs(g, 0, 1) -> 4
    adjacentBombs(g, 1, 1) -> 5
  '''
  # Observation:
  # For any position (x,y)
  # All the potential neighbours
  # are the positions (x-1, y-1), (x+0, y-1), (x+1, y-1)
  #                   (x-1, y+0),   ....    , (x+1, y+0)
  #                   (x-1, y+1), (x+0, y+1), (x+1, y+1)
  # So, these are the permutations of the deltas of x and y
  # of (-1, 0, 1) (the potential deltas),
  # except for the permutation (0,0) which is
  # our original square.
  # So, we can effectively write this code by iterating
  # over these deltas
  perms = deltaGen(LL(-1, 0, 1), LL(-1, 0, 1))
  # Now that we have perms
  # All we need to do is count for each pair
  # of the form (xd, yd) we want to check
  # is (x+xd, y+yd) a bomb or not!
  # if it is, count it
  def countBombs(pairs):
    # give pairs of x and y deltas
    # count the number of Bs
    if isEmpty(pairs):
      return 0
    pair = first(pairs)
    yd = first(rest(pair))
    xd = first(pair)
    # Must verify first that y+yd and x+xd are
    # within the bounds of our grid
    newY = y + yd
    newX = x + xd
    if newY < 0 or newY >= len(grid) or newX < 0 or newX >= len(grid[newY]):
      # If the neighbour coordinate is out of bounds then the answer is
      # the recursive result --- we can't have a bomb out of bounds!
      return countBombs(rest(pairs))
    isBomb = grid[y+yd][x+xd]
    return (1 if isBomb == "B" else 0) + countBombs(rest(pairs))
  # If using recursive helper we wrote then adjacent bombs just becomes:
  '''
  return countBombs(perms)
  '''
  # For each pair of deltas (xd, yd) what is the process we want to do?
  neighbourPos = map(lambda p: LL(x+first(pair), y+first(rest(pair))
