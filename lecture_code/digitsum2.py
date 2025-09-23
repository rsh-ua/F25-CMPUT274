
def digitSum(n):
  if n < 10:
    return n
  return n%10 + digitSum(n//10)
