from cmput274 import *


def lookup(name, names, values):
  # Remove the "pass" line and fill in this function.
  # Don't forget to include your function specification
  # docstring at the beginning of the function!
  pass


def main():
  names = LL("a", "b", "c", "d")
  values = LL(10, 15, 77, 23)
  testExact("basic1", empty(), lookup, "x", names, values)
  testExact("basic2", LL(77), lookup, "c", names, values)
  # Add your own test cases here, before the call to runTests

  runTests()

if __name__ == "__main__":
  main()
