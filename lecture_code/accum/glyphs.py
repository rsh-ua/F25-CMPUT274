from cmput274 import *
def isOpenGlyph(c):
  return c == "{" or c == "[" or c == "("

def isCloseGlyph(c):
  return c == "}" or c == "]" or c == ")"

def glyphMatch(open, close):
  if open == "{" and close == "}":
    return True
  if open == "[" and close == "]":
    return True
  if open == "(" and close == ")":
    return True
  return False

def balancedAcc(s, acc):
  '''
  balancedAcc is an accumulative recursive function
              for solving if the enclosing glyphs of
              a string s are balanced. s is the remaining
              string to check and acc is a LList of
              all the opening glyphs I've seen so far
              in the reverse order I've seen them
              such that first(acc) is the most recently
              seen opening glyph

  s       - a string
  acc     - LList of opening glyphs
  returns - bool, True if s is balanced, False otherwise

  Examples:
    balancedAcc('{[xt(y)]z}[hello]', empty()) -> True
    balancedAcc('{[(]})', empty()) -> False
  '''
  if s == "":
    # If I've reached the empty string
    # either all of my open parens were matched
    # or they weren't. If they were acc is empty
    # and the string is balanced.
    # If they weren't acc is not empty and the
    # string is not balanced!
    return isEmpty(acc)
  if isOpenGlyph(s[0]):
    # If I see an opening Glyph add it to my
    # accumulator and recurse.
    return balancedAcc(s[1:], cons(s[0], acc))
  if isCloseGlyph(s[0]):
    # If I see a closing glyph
    # and the last seen opening glyph does
    # not match then this string is not
    # balanced.
    return not isEmpty(acc) and glyphMatch(first(acc), s[0]) and balancdAcc(s[1:], rest(acc))
  # If the first character is not a glyph
  # I care about, then simply ignore it
  # and check if the rest of the string
  # is balanced
  return balancedAcc(s[1:], acc)

def balancedGlyphs(s):
  return balancedAcc(s, empty())
