def streq(s1, s2):
  '''
  streq returns True if its parameters are equal
        False otherwise

  s1     - a str
  s2     - a str
  return - a bool

  Examples:
    streq("apple", "abc") -> False
    streq("hello", "hello") -> True
  '''
  if s1 == "" and s2 == "":
    return True
  if s1 == "" or s2 == "":
    return False

  return s1[0] == s2[0] \
        and streq(s1[1:], s2[1:])

