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
  import random
  

def main():
  hand = LL(LL(13, 2), LL(2, 3), LL(7, 1),
            LL(14, 0), LL(4, 3), LL(10, 0))

  hand = mergeSort(hand, suitOrder)
  displayHand(hand)


if __name__ == "__main__":
  main()
