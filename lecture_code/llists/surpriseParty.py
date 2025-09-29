from cmput274 import *

def digitToNumber(c):
  '''
  digitToNumber returns the integer value that represents
                the single digit character provided

  c       - is a single character string, containing
            only a digit character
  returns - an integer in the range [0,9]

  Examples:
    digitToNumber("0") -> 0
    digitToNumber("5") -> 5
  '''
  # The observation here, is that the digits are
  # sequential in the ASCII table, that means
  # that if the ASCII value for "0" is x
  # then for "1" it is x+1
  # for "2" it is x+2
  # ...
  # for "9" it is x+9

  # Therefore, for any digit the integer
  # value is ord(digit) - x
  # that x is ord("0") as defined above!
  return ord(c) - ord("0")

def timeUnitToNum(s):
  '''
  timeUnitToNum takes a two digit string and
                returns the integer it represents!

  s       - a two digit string
  returns - integer

  Examples:
    timeUnitToNum("05") -> 5
    timeUnitToNum("47") -> 47
  '''
  tensDigit = digitToNumber(s[0])
  onesDigit = digitToNumber(s[1])
  return tensDigit*10 + onesDigit

def timeToMins(s):
  '''
  timeToMins returns the minutes since midnight represented
             by the given time string.

  s       - A string of the form "HH:MM" where HH is 00-23
            and MM is 00-59
  returns - an integer, the minutes since midnight

  Examples:
    timeToMins("03:25") -> 205
    timeToMins("14:57") -> 897
  '''
  return timeUnitToNum(s[0:2])*60 + timeUnitToNum(s[3:5])


def timeToEnter(lot, dur):
  '''
  timeToEnter finds a time that it is possible
              to enter a house and throw a surprise
              party without ruining the surprise
              (gettin caught), if no time is possible
              returns False

  lot     - list of strings of the form "HH:MM",
            and the elements of the list are
            (e1,r1,e2,r2,...,en,rn) where ei
            is the ith time the person left their
            house and ri is the ith time that they
            returned to the house
  dur     - an integer, represents number of minutes
            needed to throw a surprise party
  returns - the first time string that begins a long
            enough duration, or False

  Examples:
    times = cons("03:20", cons("07:45", cons("11:30", cons("18:10", empty()))))
    timeToEnter(times, 180) -> "03:20"
    timeToEnter(times, 300) -> "11:30"
    timeToEnter(times, 1200) -> False
  '''
  if isEmpty(lot):
    return False
  exitTime = first(lot)
  returnTime = first(rest(lot))
  timeGone = timeToMins(returnTime) - timeToMins(exitTime)
  if timeGone < dur:
    # if my list is of the form (e1, r1, e2, r2, ..., en, rn)
    # and I just realized that e1 r1 is a useless pair of values
    # AND my function expects that I call it on a list
    # in this format
    # can I even call my function on rest(lot)?
    # rest(lot) would be the list of form
    # (r1, e2, r2, ..., en, rn)
    # That violates the expectation of our function!
    # we have an r1 without a preceding e1!
    # What we want is to remove this PAIR
    # so, rest(rest(lot))
    return timeToEnter(rest(rest(lot)), dur)
  # if timeGone >= dur then this IS enough time
  # to throw a surprise party. So, we can return
  # exitTime as the safe time to enter to setup
  # the party
  return exitTime
