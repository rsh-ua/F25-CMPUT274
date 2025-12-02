import sys
def main():
  if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} int")
    sys.exit(1)
  n = int(sys.argv[1])
  lineNo = 1
  while n > 0:
    line = input()
    print("Line number " + str(lineNo) + " contents: " + repr(line))
    n = n - 1
    lineNo = lineNo + 1

if __name__ == "__main__":
  main()
