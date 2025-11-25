
someNum = 7

def f(n):
  x = 5
  def g(y):
    # which x is this?
    x = 10
    # Does this change f's x when called?
    return y+x
  g(7)
  # It did no! f(2) returns 5*2 not 10*2
  return x*n


def foo(n):
  x = 3
  def bar(t):
    return t*x+someNum
  return x*bar(n)

def hmm(n):
  foo(5)
  return n*x
