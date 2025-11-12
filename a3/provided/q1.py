from cmput274 import *


def main():
  testExact("basic1", 1, hammingDistance, "axyz", "axzz")
  testExact("basic1", 4, hammingDistance, "abc----", "abc")
  testExact("basic1", 3, hammingDistance, "grey", "hazy")
  # Add your own test cases here, before the call to runTests

  runTests()

if __name__ == "__main__":
  main()
