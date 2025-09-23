def pigLatinVowel(s):
  '''
  See slides
  '''
  return s + "way"

def pigLatinCons(s):
  '''
  See slides
  '''
  return s[1:] + s[0] + "ay"

def pl(s):
  '''
  pl translates an alphabetic string to its
     pig latin version

  s       - an alphabetic string
  Returns - An alphabetic string

  Examples:
  pl("hello")  -> "ellohay"
  pl("orange") -> "orangeway"
  '''
  # Need to ask if s[0] is a vowel or not
  if s[0] == "a":
    return pigLatinVowel(s)
  if s[0] == "e":
    return pigLatinVowel(s)
  if s[0] == "i":
    return pigLatinVowel(s)
  if s[0] == "o":
    return pigLatinVowel(s)
  if s[0] == "u":
    return pigLatinVowel(s)
  return pigLatinCons(s)
