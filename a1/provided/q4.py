from cmput274 import *
# The above line should appear at the start of
# all of your CMPUT274 programs

def isPrime(n):
  # Remove the "pass" line and fill in this function.
  # Don't forget to include your function specification
  # docstring at the beginning of the function!
  pass


def main():
  testExact("basic1", True, isPrime, 7)
  testExact("basic2", False, isPrime, 91)
  # Write your own test cases here as you see fit.
  # You should write many test cases to make yourself
  # confident your solution works before you hand it in!
  runTests()

if __name__ == "__main__":
  main()
