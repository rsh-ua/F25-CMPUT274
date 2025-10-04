from cmput274 import *

def isIntegerStr(s):
  # Remove the "pass" line and fill in this function.
  # Don't forget to include your function specification
  # docstring at the beginning of the function!
  pass


def main():
  testExact("basic1", True, isIntegerStr, "456")
  testExact("basic2", False, isIntegerStr, "43-3")
  # Place your test cases here, before the runTests call.

  runTests() 


if __name__ == "__main__":
  main()
