from cmput274 import *
def strSplit(s, sep):
  # Remove the "pass" line and fill in this function.
  # Don't forget to include your function specification
  # docstring at the beginning of the function!
  pass


def main():
  testExact("basic1", LL("123", "abcdf", "hello"), strSplit, "123,abcdf,hello", ",")
  # Add your own test cases here, before the call to runTests

  runTests()

if __name__ == "__main__":
  main()
