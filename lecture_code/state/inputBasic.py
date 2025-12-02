def main():
  # The input function would have a function
  # specification something like this:
  '''
  input prints its argument to the screen
        and reads the string from the input
        stream up until the next newline
        character (or EOF) and returns
        that string, also removes the first
        newline it sees from the input stream

  msg    - str, message to display to the screen
  return - str, the string read in

  Side effects:
    - prints msg to the screen
    - reads characters from the input stream
      up to and including the first newline seen
      or the EOF

  Examples:
    I <- "hello\nthere\nfriend\n"
    input("foo") -> "hello"
      # message "foo" is printed to the screen
      # AND I is mutated to be
      # "there\nfriend\n"
  '''
  x = input()
  print("X's value: " + repr(x))

  y = input("This is a message")
  print("Y's value: " + repr(y))

  z = input("Nicer input message: ")
  print("Z's value: " + repr(z))

if __name__ == "__main__":
  main()
