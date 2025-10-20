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

def LL(*args):
  '''
  LL is a function for easily creating a LList from an arbitrary
     list of values

  returns - A LList
  *args   - A comma separated list of values. That means you can
            call LL with any number of arguments, which should be
            the values you want in your LList in order.

  Examples:
    LL(1, 2, 3) -> cons(1, cons(2, cons(3, empty())))
    LL("a", 10, 2, "goodbye") -> cons("a", cons(10, cons(2, cons("goodbye", empty()))))
  '''
  return foldr(args, lambda x, y : cons(x, y), empty())


def foldr(l, fn, base):
  '''
  foldr folds the given function over the iterable
        object, using base as the terminal value
        Performs a right fold.

  l       - an iterable object, e.g. a LList
  fn      - A function with two parameters
            The first of which must match the type of the
            items in l, and the second of which must
            match the type of the return value 
            of fn as well as the type of base
  base    - A value, type must match the expected
            type of the second parameter of fn
  returns - The result of right-folding fn over the list,
            Type is the return type of fn

  Examples
    foldr(LL(1,2,3), lambda x, y: x + y, 0) -> 6
    foldr(LL(1,2,3), lambda x, y: cons(x, y), LL(4,5,6)) -> (1, 2, 3, 4, 5, 6)
  '''
  return trampoline(_foldrtco(iter(foldl(l, lambda x, y: cons(x, y), empty())), fn, base))

def foldl(l, fn, acc):
  '''
  foldl folds the given function over the iterable
        object, using base as the terminal value
        Performs a left fold.

  l       - an iterable object, e.g. a LList
  fn      - A function with two parameters
            The first of which must match the type of the
            items in l, and the second of which must
            match the type of the return value 
            of fn as well as the type of base
  base    - A value, type must match the expected
            type of the first parameter of fn
  returns - The result of left-folding fn over the list,
            Type is the return type of fn

  Examples
    foldl(LL(1,2,3), lambda x, y: x + y, 0) -> 6
    foldl(LL(1,2,3), lambda x, y: cons(x, y), LL(4,5,6)) -> (3, 2, 1, 4, 5, 6)
  '''
  return trampoline(_foldltco(iter(l), fn, acc))

def map(f, l):
  '''
  map maps the given unary function f onto the LList l
      and returns the result of that mapping.

  f       - (X->Y)
  l       - LList of X
  returns - LList of Y

  Examples:
    map(lambda x: x+2, LL(1, 2, 3)) -> LL(3, 4, 5)
  '''
  return foldr(l, lambda x, y: cons(f(x), y), empty())


def filter(f, l):
  '''
  filter filters the LList l using the given predicate f
      and returns the result of that filter.

  f       - (X->bool)
  l       - LList of X
  returns - LList of X

  Examples:
    filter(lambda x: x%2==1, LL(1, 2, 3)) -> LL(1, 3)
  '''
  return foldr(l, lambda x, y: cons(x, y) if f(x) else y, empty())


#######################################################
'''
Everything below here is implementation details,
and not part of the interface that CMPUT274 students
need to concern themselves with. There is no need
to read or understand the code below this point.

For this reason, code below this point is lacking in 
function specifications or documentation. The intent
is that CMPUT 274 students do not need to understand
or know of the existence of the code below.
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

  def __eq__(self, rhs):
    if not isinstance(rhs, _LList):
      return False
    if self._len != rhs._len:
      return False
    if isEmpty(self) and isEmpty(rhs):
      return True
    return first(self) == first(rhs) and rest(self) == rest(rhs)
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

def a1Code():
  from functools import reduce
  return reduce(lambda x, y: f"{y}{x}{y}", cons("welcome", cons("cmput274", cons("student", empty()))), "")



def TCO(func):
  '''
  TCO is a function decorator that can be used on a function
      that is trivially tail-recursive in order to apply
      tail-call optimization to that function.

      A function is trivially tail-recursive if its return
      statements are either:
      - A final value that can be calculated (i.e. base case)
      - A recursive case that ONLY returns the result of recursion
        e.g. 
        return recFn(...) is good
        return 1+recFn(...) is no good
  '''
  from functools import wraps
  if not hasattr(TCO, "fn"):
    setattr(TCO, "fns", dict())
  @wraps(func)
  def wrapper(*args, **kwargs):
    from ast import parse
    from inspect import getsource
    if TCO.fns.get(func) != None:
      return TCO.fns[func](*args, **kwargs)
    import types
    ast = parse(getsource(func))
    fnName = ast.body[0].name
    tcoAst = _TCOTransformer(fnName).visit(_DecoratorRemover().visit(ast))
    compiled = compile(tcoAst, __name__, "exec")
    oldItems = list(globals().items())
    exec(compiled, globals())
    for item in globals().items():
      if item[0] != "oldItems" and item not in oldItems:
        if isinstance(item[1], types.FunctionType):
          TCO.fns[func] = item[1]
    return TCO.fns[func](*args, **kwargs)

  return wrapper

from ast import NodeVisitor, NodeTransformer

class _Thunk:
  def __init__(self, fn, *args, **kwargs):
    self._fn = fn
    self._args = args
    self._kwargs = kwargs

  def _apply(self):
    return self._fn(*self._args, **self._kwargs)

class _TCOTransformer(NodeTransformer):
  def __init__(self, name):
    '''
    name - Name of function being transformed
           used to ensure that there is no return statement
           that isn't trivially tail call optimizable
    '''
    self._name = name

  def visit_Return(self, node):
    from ast import Call, copy_location, Name, Return, Load
    if node.value.__class__ == Call:
      fn = node.value.func
      args = node.value.args
      newFn = copy_location(Name(id="_makeThunk", ctx=Load()), node.value.func)
      newCall = copy_location(Call(func=newFn, args =[fn]+args, keywords=node.value.keywords), node.value)
      return copy_location(Return(value=newCall), node)
    else:
      if _ASTContains(self._name).visit(node):
        raise BadTCO(f"Cannot tail call optimize {self._name} as it has a recursive case that does not simply return the result of recursion.")
      return node

class BadTCO(Exception):
  '''
  Exception to be generated when @TCO decorator is
  used incorrectly
  '''
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return self.msg

class _ASTContains(NodeVisitor):
  def __init__(self, name):
    self._name = name

  def visit_Call(self, node):
    from ast import Name
    fn = node.func
    if type(fn) == Name:
      if fn.id == self._name:
        return True
    return self.generic_visit(node)
  
    
  def generic_visit(self, node):
    from ast import iter_child_nodes
    b = False
    for child in iter_child_nodes(node):
      b = b or self.visit(child)
    return b
  
def _applyThunk(b):
  return b._apply()

def _makeThunk(fn, *args):
  return _Thunk(fn, *args)

def trampoline(p):
  while type(p) == _Thunk:
    p = _applyThunk(p)
  return p

class _DecoratorRemover(NodeTransformer):
  def visit_FunctionDef(self, node):
    node.decorator_list = []
    return node
  
@TCO
def _foldltco(it, fn, acc):
  try:
    val = next(it)
  except StopIteration:
    return acc
  return _foldltco(it, fn, fn(val, acc))



@TCO
def _foldrtco(it, fn, acc):
  try:
    val = next(it)
  except StopIteration:
    return acc
  return _foldrtco(it, fn, fn(val, acc))


  
# Set recursion limit so student programs have a larger recursion limit.
# All student programs should import this module, meaning this should
# run for all student programs.

import sys
sys.setrecursionlimit(5000)
