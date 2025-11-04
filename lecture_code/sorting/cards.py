from cmput274 import *


'''
A Card is a
- LL(Rank, Suit)
'''

'''
A Rank is one of
- 2-10
- "J"
- "Q"
- "K"
- "A"
'''

'''
A Suit is one of
- "♣"
- "♠"
- "♦"
- "♥"
'''

# For example
# LL(2, "♦") -> Two of Diamonds
# LL("Q", "♥") -> Queen of Hearts

# We want to be able to sort a hand of cards such as

hand = LL(LL("K", "♥"),
          LL(2, "♠"),
          LL(7, "♣"),
          LL("A", "♦"),
          LL(4, "♠"),
          LL(10, "♦"))
# Sorting this hand should sort based on suited order
# ascending ranks within suits.
# The suited order is Diamond, Clubs, Hearts, Spades
# So this hand sorted should render
'''
LL(LL(10, "♦"), LL("A", "♦"), LL(7, "♣"),
   LL("K", "♥"), LL(2, "♠"), LL(4, "♠"))
'''

second = lambda l: first(rest(l))

def rankToNum(c):
  '''
  Returns the natural number representation
  of the rank of the given card

  c - Card
  '''
  rank = first(c)
  if rank == "J":
    return 11
  if rank == "Q":
    return 12
  if rank == "K":
    return 13
  if rank == "A":
    return 14
  return rank

def suitToNum(c):
  '''
  Return the num corresponding to suit
  of Card c
  '''
  suit = second(c)
  if suit == "♠":
    return 3
  if suit == "♥":
    return 2
  if suit == "♣":
    return 1
  if suit == "♦":
    return 0

def compCard(c1, c2):
  '''
  compCard compares two cards, returns
           true if c1 > c2, False otherwise

  c1 - Card
  c2 - Card
  returns - bool

  Examples:
    compCard(LL("K", "♥"), LL(4, "♠")) -> False
    compCard(LL(2, "♣"), LL(6, "♦")) -> True
  '''
  if second(c1) == second(c2):
    # Suits are the same, must compare ranks
    return rankToNum2(c1) > rankToNum2(c2)
  return suitToNum2(c1) > suitToNum2(c2)


'''
rankToNum and suitToNum are gross...
they're a bunch of ifs. If we add another
suit, we need to go in and add a whole new
if statement to our suitToNum

Worse! If we want this new suit
to be "inserted" in order between
two of our existing suits we'd
need to also change that code

How could we write these functions better?

Note: we are effectively mapping strings
      to sequential naturals.
      Where else have we seen values
      have a mapping to sequential naturals?

      LL("A", "T", "P")
          0,   1,   2
     indices of a sequential data type are mappings
     between arbitrary values and sequential naturals!
'''
def index(v, l):
  if v == first(l):
    return 0
  return 1 + index(v, rest(l))


def rankToNum2(c):
  rank = first(c)
  ranks = LL(2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
  return index(rank, ranks) + 2

def suitToNum2(c):
  suit = second(c)
  suits = LL("♦", "♣", "★", "♥", "♠")
  return index(suit, suits)
