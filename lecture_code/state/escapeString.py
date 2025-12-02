from cmput274 import *

def escapeString(s):
  '''
  escapeString takes a string that includes
               literal backslashes followed
               by characters that are meant
               to represent escaped character
               this function returns a version
               of the string that replaces those
               pairs of characters with the single
               escape character it is meant to
               represent

  s       - str
  returns - str

  Side effects: None

  Examples:
    escapeString("hello\\nfriend\\tyay")
      -> "hello\nfriend\tyay"
  '''
  def fixEscape(c, s):
    if c != "\\":
      return c + s
    # If it is a backslash, look at the
    # character that follows it (the first of s)
    # and combine them into an escape characeter
    if s[0] == "n":
      return "\n" + s[1:]
    elif s[0] == "t":
      return "\t" + s[1:]
    elif s[0] == "\\":
      return "\\" + s[1:]
    else: # else if it is not one of our valid escapes
      # If the character following this backslash is
      # not a valid escape character then this should
      # be a backslash!
      return c + s
  return foldr(s, fixEscape, "")

def main():
  # Write the main that executes until
  # the user enters the string "quit"
  # as input. Each time the user enters
  # a string that is NOT "quit"
  # the program will apply
  # escapeString to the string the user
  # entered and print out the repr
  # and the string itself
  # of the newly escaped string
  line = input()
  while line != "quit":
    escaped = escapeString(line)
    print("Original repr: " + repr(line))
    print(line)
    print("Escaped repr: " + repr(escaped))
    print(escaped)
    line = input()


if __name__ == "__main__":
  main()
