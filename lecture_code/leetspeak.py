def convertChar(c):
  '''
  convertChar converts an individual character into
              its leetspeak counterpart

  c      - is string containing one character
  return - string containing one character

  Examples:
    convertChar("a") -> "4"
    convertChar("w") -> "w"
  '''
  if c == "A" or c == "a":
    return "4"
  if c == "L" or c == "l":
    return "1"
  if c == "T" or c == "t":
    return "7"
  if c == "e" or c == "E":
    return "3"
  if c == "S" or c == "s":
    return "5"
  if c == "o" or c == "O":
    return "0"
  return c

def leetSpeak(s):
  if s == "":
    return ""
  if s == "er" or s == "Er" or s == "eR" or s == "ER":
    return "z0r"
  return convertChar(s[0]) + leetSpeak(s[1:])
