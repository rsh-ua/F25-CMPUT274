
from cmput274 import *
def multTables(m, n):
  '''
  multTables returns the mxn multiplication table

  m - Nat
  n - Nat
  returns - LList of (LList of Nat)

  Examples:
    multTable(3, 2)
      -> LL(LL(1, 2),
	          LL(2, 4),
	          LL(3, 6))
    multTable(5, 4)
      -> LL(LL(1, 2, 3, 4),
	          LL(2, 4, 6, 8),
	          LL(3, 6, 9, 12),
	          LL(4, 8, 12, 16),
	          LL(5, 10, 15, 20))
  '''

  # Multi dimensional data is new,
  # which can be at first confusing
  # we may not know where to begin
  # writing a recursion that produces
  # a LList of LLists!
  # That's because that is hard to do!
  # The easier thing is to continue what
  # we've been doing and break down problems
  # into smaller sub problems.

  # So we observe that really all we're doing
  # is building a LList of /rows/ of a multiplication
  # table.

  # Therefore, all we need is a function that produces
  # a /row/ and to recursively build a list using
  # that function.

  # So ignore the LList of LLists of it alll
  # and instead solve the problem
  # how do we build the LList(row(1), row(2), row(3), ... row(n))

  # multTables(m, n) -> LList m rows
  # What is our base case?
  # 0 rows!
  def row(i):
    return map(lambda x: x*i, buildList(lambda x: x+1, n))
  l = buildList(lambda x: x+1, m)
  return map(row, l)

reverse = lambda l: foldl(l, cons, empty())

def multTablesRecHelper(m, n):
  def row(i, n):
    # This builds the ith row
    # of a multiplication table
    # with n columns
    if n == 0:
      # The row with 0 columns is trivial
      return empty()
    return cons(i*n, row(i, n-1))
  # We are building the table of
  # m rows, each row is n columns long
  # so our base case is the table
  # with 0 rows.
  if m == 0:
    # the table with 0 rows is trivial
    return empty()
  # if m is NOT 0, we must construct the
  # current row and add it to our answer
  # Assume we have the function row(i, n)
  # that constructs the ith multiplication
  # table row with n columns
  return cons(reverse(row(m, n)), multTablesRecHelper(m-1, n))

def multTablesRec(m, n):
  return reverse(multTablesRecHelper(m,n))
