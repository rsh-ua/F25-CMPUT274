

def strlen(s):
  '''
  strlen returns the length of a given string

  s      - str
  return - an integer, the length of the str

  Examples:
    strlen("abc") -> 3
    strlen("hello") -> 5
    strlen("") -> 0
  '''
  if s == "":
    return 0
  return 1 + strlen(s[1:])
