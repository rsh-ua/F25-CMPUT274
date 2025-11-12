from cmput274 import *

def main():
  nonDec = lambda x, y: x <= y
  testExact("basic1", LL(1, 7, 10, 12), optimalPurgeSort, LL(1, 9, 7, 13, 10, 12), nonDec)
   # Add your own test cases here, before the call to runTests

  runTests()

if __name__ == "__main__":
  main()
