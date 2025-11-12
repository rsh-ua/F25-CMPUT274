from cmput274 import *


def main():
  testExact("basic1", LL(LL("cook", 3), LL("the", 2), LL("not", 1)), wordCounts, "cook the cook not the cook")
  testExact("basic2", LL(LL("also", 1),
                         LL("don't.", 1),
                         LL("Also", 1),
                         LL("don't", 1)), wordCounts, "also don't.\n\nAlso   don't")

  # Add your own test cases here, before the call to runTests

  runTests()


if __name__ == "__main__":
  main()
