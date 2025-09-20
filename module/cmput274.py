'''
Module for use with CMPUT 274 at the University of Alberta

Includes many definitions used for the class.

As tools become necessary, new tools will be added to this module.
'''



def testExact(name : str, expected : any, fn: callable, *args : any):
  '''
  testExact is a function used to write test cases
             for functions that produce a value that
             is testable for an /exact/ match. This is
             most values in CMPUT 274 except floats.

  name     - str, name of this test case
  expected - the expected result of the test case, same as fn return type.
  fn       - the function to be tested
  args     - all the arguments to be provided to fn for this test case.
  returns  - Nothing, adds test case to the set of test cases to be executed
             when runTests is executed.

  Example:
    testExact("t1", 45, max, -12, 45, 33, 17) -> Test Passed
    testExact("t2", "wow", lambda x, y: x + y, "wo", "ow") -> Test Failed
  '''
  _register(tuple([name, lambda : (f"{name} passed" if fn(*args) == expected else 
                                  f"{name} failed expected:\n{repr(expected)}\nreceived:\n{repr(fn(*args))}") + "\n"+"-"*20]))

def testWithin(name : str, expected : float, err : float, fn : callable, *args : any):
  '''
  testWithin is a function used to write test cases
              for functions that produce a value that
              is not testable for an /exact/ match.
              Typically this is only floats in this course.

  name     - str, name of this test case
  expected - the expected result of the test case, same as fn return type.
  err      - same type as expected. [expected-err, expected+err] is the
             acceptable range for the value produced by the function.
  fn       - the function to be tested
  args     - all the arguments to be provided to fn for this test case.
  returns  - Nothing, adds test case to the set of test cases to be executed
             when runTests is executed.

  Example:
    def pyth(a, b):
      from math import sqrt
      return sqrt(a**2+b**2)
    testWithin("t1", 5.8, 0.04, pyth, 5, 3) -> Test Passed
    testWithin("t2", 5.8, 0.03, pyth, 5, 3) -> Test Failed
  ''' 
  _register(tuple([name, lambda : (f"{name} passed" if (fn(*args) < expected + err and fn(*args) > expected - err) else 
                                  f"{name} failed expected:\n{expected}±{err}\nreceived:\n{fn(*args)}") + "\n"+"-"*20]))



def runTests():
  '''
  runTests executes all the tests that have been created with testWithin or testExact
           and displays the results

  returns - Nothing

  Side Effects: prints a message to the screen for each test case that has been created.

  Examples:
    def pyth(a, b):
      from math import sqrt
      return sqrt(a**2+b**2)
    testWithin("t1", 5.8, 0.04, pyth, 5, 3)
    testWithin("t2", 5.8, 0.03, pyth, 5, 3)
    runTests() -> None
      Prints:
      t1 passed
      t2 failed expected:
      5.8±0.03
      received:
      5.830951894845301
  '''
  _register(1, True)

'''
The following functions operate on an abstract data type (ADT) that we will refer to as
an LList. The data definition for an LList is as follows. An LList is one of

- empty
- cons(elem, LList)

Where elem can be any type. The cons function constructs a new LList by prepending the given elem to the
given LList. As such, we can construct an LList that represents the sequence 1, 2, 3 by doing the following
function calls defined below:

cons(1, cons(2, cons(3, empty())))

As LList is our ADT, it can only be constructed and operated on through the functions below. Any manipulations
to the data type through other means than the functions below invaldiate it as an LList.

For shorthand, we will represent textually the value of an LList constructed as 
cons(a1, cons(a2, ...cons(an, empty())))
as 
(a1, a2, ..., an)
'''

def empty():
  '''
  empty produces an empty LList, for constructing.

  returns - An empty LList

  Examples:
    empty() -> ()
  '''
  return _LList()

def first(l):
  '''
  first returns the first element in a non-empty LList

  l       - a non-empty LList
  returns - the first element of l

  Examples:
    first(cons(1, cons(2, cons(3, empty())))) -> 1
    first(cons(cons(1, empty()),
               empty())) -> (1)
  '''
  return l._car()

def rest(l):
  '''
  rest returns an LList that represents all elements in a
       non-empty LList without its first element.

  l       - a non-empty LList
  returns - an LList

  Examples:
    rest(cons(1, cons(2, cons(3, empty()))))
  '''
  return l._cdr()

def cons(elem, l):
  '''
  cons returns an LList constructed by prepending a given element
       to the given LList

  elem    - any, an item to be placed in an LList
  l       - an LList
  returns - an LList

  Examples:
    cons(1, empty()) -> (1)
    cons(1, cons(2, empty())) -> (1, 2)
  '''
  return l._cons(elem)

def isEmpty(l):
  '''
  isEmpty returns True if the given LList is empty, False otherwise

  l       - an LList
  returns - bool

  Examples:
    isEmpty(empty()) -> True
    isEmpty(cons(1, empty())) -> False
    isEmpty(cons(empty(), empty())) -> False
  '''
  return l._isEmpty()

#######################################################
'''
Everything below here is implementation details,
and not part of the interface that CMPUT274 students
need to concern themselves with. There is no need
to read or understand the code below this point.
'''
#######################################################

class _LList:
  class _LListIter:
    def __init__(self, t):
      self._data = t
    
    def __next__(self):
      if self._data != ():
        val = self._data[0]
        self._data = self._data[1]
        return val
      else:
        raise StopIteration

  def __init__(self, data=(), l=0):
    self._data = data
    self._len = l



  def __iter__(self):
    return _LList._LListIter(self._data)

  def _cons(self, elem):
    return _LList((elem, self._data), self._len+1)

  def _car(self):
    assert not self._isEmpty()
    return self._data[0]
  
  def _cdr(self):
    assert not self._isEmpty()
    return _LList(self._data[1], self._len-1)
  
  def _isEmpty(self):
    return self._len == 0
  
  @staticmethod
  def _reprHelper(t):
    if t == ():
      return ""
    if t[1] == ():
      return f"{repr(t[0])}"
    return f"{repr(t[0])}, {_LList._reprHelper(t[1])}"


  def __repr__(self):
    return f"({self._reprHelper(self._data)})"



def statics(**kwargs):
  def decorate(func):
    for k in kwargs:
      setattr(func, k, kwargs[k])
    return func
  return decorate

@statics(reg=())
def _register(fn, run=False):
  if not run:
    _register.reg = _register.reg + (fn,)
  else:
    if _register.reg != ():
      print("-"*20)
    else:
      print("No tests to run!")
    for f in _register.reg:
      try:
        print(f[1]())
      except Exception as e:
        print(f"Test {f[0]} caused an error and was unable to be executed")
        print(f"Error: {e}")
    _register.reg = tuple()

# Set recursion limit so student programs have a larger recursion limit.
# All student programs should import this module, meaning this should
# run for all student programs.

def a1Code():
  from functools import reduce
  return reduce(lambda x, y: f"{y}{x}{y}", cons("welcome", cons("cmput274", cons("student", empty()))), "")

import sys
sys.setrecursionlimit(5000)