from cmput274 import *

def removeOccurrences(l, toRemove):
  # Remove the "pass" line and fill in this function.
  # Don't forget to include your function specification
  # docstring at the beginning of the function!
  pass

def main():
  testExact("basic1", LL(1, 5, 22, 33), removeOccurrences,
            LL(1, 5, 10, 22, 10, 33), 10)
  testExact("basic2", LL("hello", "goodbye", "my", "friend"), removeOccurrences,
            LL("", "hello", "", "", "goodbye", "", "my", "", "friend", ""), "")
  # Place your test cases here, before the runTests call.

  runTests()
if __name__ == "__main__":
  main()
