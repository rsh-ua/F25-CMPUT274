from cmput274 import *


'''
A Card is a
- LL(Rank, Suit)
'''

'''
A Rank is
- an int in range [2, 14]
'''

'''
A Suit is
- an int in range[0,3]
'''
def takeN(l, n):
  # Returns a LList of the first n items of l
  if n == 0:
    return empty()
  return cons(first(l), takeN(rest(l), n-1))

def skipN(l, n):
  # Returns a LList of all except the first n items of l
  if n == 0:
    return l
  return skipN(rest(l), n-1)

def mergeSort(l, cmp):
  def merge(sl1, sl2):
    if isEmpty(sl1):
      return sl2
    if isEmpty(sl2):
      return sl1
    if cmp(first(sl1), first(sl2)):
      return cons(first(sl1), merge(rest(sl1), sl2))
    return cons(first(sl2), merge(sl1, rest(sl2)))
  if len(l) <= 1:
    return l
  leftHalf = mergeSort(takeN(l, len(l)//2), cmp)
  rightHalf = mergeSort(skipN(l, len(l)//2), cmp)
  return merge(leftHalf, rightHalf)

def suitOrder(c1, c2):
  if second(c1) < second(c2):
    return True
  if second(c1) > second(c2):
    return False
  return first(c1) < first(c2)

def displayHand(hand):
  '''
  displayHand displays a hand of cards in a user friendly way
              to the user

  hand    - LList of Cards
  returns - None

  Side Effects: prints the hand to the screen

  Examples:
  hand = LL(LL(13, 2), LL(2, 3), LL(7, 1),
            LL(14, 0), LL(4, 3), LL(10, 0))
  displayHand(hand) -> None
      The string "|K♥|2♠|7♣|A♦|4♠|X♦|\n" is printed to the screen
  '''
  def cardToStr(c):
    suits = ("♦", "♣", "♥", "♠")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9",
             "X", "J", "Q", "K", "A")
    return ranks[first(c)-2] + suits[second(c)]

  los = map(cardToStr, hand)
  outString = "|" + foldr(los, lambda cardS, ror : cardS + "|" + ror, "")
  print(outString)

def replaceInd(l, i, val):
  '''
  returns a version of LList l
  where the ith item has been replaced
  with val

  Assumes i is a valid index of l
  '''
  if i == 0:
    return cons(val, rest(l))
  return cons(first(l), replaceInd(rest(l), i-1, val))

def askDiscard(hand):
  '''
  askDiscard asks the user which card they would
             like to discard and returns a new
             hand with that card discarded and
             a random one drawn

  hand    - LList of Card
  returns - LList of Card

  Side effects:
    - Print a message to the screen
    - Reads a line of input from the input stream

  Examples:
    I <- "2\n"
    askDiscard(LL(LL(13, 2), LL(2, 3), LL(7, 1),
                LL(14, 0), LL(4, 3), LL(10, 0))
    # Randomly generates 6 and 2
      -> LL(LL(13, 2), LL(6, 2), LL(7, 1),
                LL(14, 0), LL(4, 3), LL(10, 0))
  '''
  # Side note here... this function would be more
  # reusable as a pure function.
  # So this function instead of being the one to
  # read input and generate a random number
  # this function should just take 3 parameters
  # first, the original hand
  # second, the index of the card to discard
  # third, the new card to insert
  # That way someone else can read input and
  # generate a random number and then simply
  # call this function. That way this function
  # can be used even in cases where we DON'T
  # get that answer from input or from a random
  # number
  # e.g. what if we change our program to pull
  # a card from an already shuffled deck?
  # or what if the card to discard does not come from the
  # input stream but from somewhere else?
  import random
  msg = "Which card number would you like to discard? [1-" + str(len(hand)) + "]: "
  # Note, as per discussion in class the above line could be replaced with
  '''
  msg = f"Which card number would you like to discard? [1-{len(hand)}]: "
  '''
  discSelection = input(msg)
  # Must convert discSelection which is a string because input returns a str
  # to an int
  # Note: they give us a number i in [1-n] meaning the ith card
  #       since we zero index the index of the ith card is
  #       i-1
  ind = int(discSelection) - 1
  # Need to generate a random card. Generating a card is
  # Generating a random rank and a random suit
  # The ranks must be in the range [2-14] and the
  # suits must be in the range[0-3]
  # The function randint in the random module
  # Takes two integer parameters start and end
  # and returns a random integer in the range
  # [start, end]
  # Since we simply wrote
  # import random
  # and not
  # from random import *
  # or
  # from random import randint
  # We did not pull the definitions from the
  # random module into our global scope
  # as such, we must specify when an identifier
  # is defined within the scope of the random
  # module.
  # We do so with the member access operator .
  # expr.ident
  # expr must be an object (any data in python)
  # and rhs must be an identifier that is
  # defined within that object
  rank = random.randint(2, 14)
  suit = random.randint(0, 3)
  card = LL(rank, suit)
  return replaceInd(hand, ind, card)

def main():
  hand = LL(LL(13, 2), LL(2, 3), LL(7, 1),
            LL(14, 0), LL(4, 3), LL(10, 0))

  hand = mergeSort(hand, suitOrder)
  displayHand(hand)
  command = input("Enter command (d, q): ")
  while command != "q":
    if command == "d":
      hand = mergeSort(askDiscard(hand), suitOrder)
      displayHand(hand)
    else:
      print(f"Invalid command {command} must be d or q")
    command = input("Enter command (d, q): ")

if __name__ == "__main__":
  main()
