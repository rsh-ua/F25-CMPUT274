from cmput274 import *
# The line above should appear in all of your assignment solutions
# at the very start.

def f1(s, c):
  '''
  This function is meant to return a new string which is the result
  of removing all occurrences of character c from string s.

  It has some bugs in it. You must write test cases that find the bugs!
  Some example test cases are provided.

  This function purposely uses concepts we have not discussed yet in class
  to make it more confusing to understand. You should not try to understand
  the code, but rather treat this function as a "black box" and write thorough
  test cases to find the bug, trying many different combinations of strings
  and characters.

  A concept being used in this code does not mean you are allowed to use that
  concept for future solutions, if it has not already been discussed in class.
  '''
  from functools import reduce
  return reduce(lambda x, y: f"{'' if ord(y) > ord(c)-1 and ord(y) <= ord(c)+1 else y}{x}", s[::-1], "")


def f2(n):
  '''
  This function is meant to estimate pi using the Madhava-Leibniz formula for pi. n is
  the number of terms used in the estimation, so the larger n the higher the precision.
  '''
  from functools import reduce
  return 4*reduce(lambda x, y: -1/y+x if (y//2)%2 else 1/y + x, [z for z in range((n)*2) if z%2])




def main():
  '''
  The "main" function is where we will write our test cases.

  Some test cases for the functions you need to test are already written,
  you must write more to catch the bugs.
  '''

  '''
  testExact is used to write test cases for functions whos return values can be tested
  for exact equality (in this class, most anything but floats or things containing floats).

  The first argument to provide to testExact is a string which is the name of the test.
  The second argument to provide to testExact is the expected value, that is the result
      you expect to be produced by the test case you are writing
  The third argument to provide to testExact is the function that is to be tested in this
      test case.
  After the third argument, there should be a number of arguments equal to the number of
      parameters the function being tested has. The order of these arguments should also
      match the order of the parameters of the function being tested. These are the
      arguments to supply to that function for the given test case.

  Full documentation of testExact is provided in the cmput274 module. It can be accessed
  by running the commands

  from cmput274 import *
  help(testExact)

  in your Python shell.
  '''

  '''
  This test case is named f1_test1 and is testing that the function call
  f1("hello", "l")
  produces the value "heo"
  '''
  testExact("f1_test1", "heo", f1, "hello", "l")
  '''
  This test case is named f1_test2 and is testing that the function call
  f1("chairs can climb out the pricey enclave", "c")
  produces the value "hairs an limb out the priey enlave"
  '''

  testExact("f1_test2", "hairs an limb out the priey enlave", f1, "chairs can climb out the pricey enclave", "c")
  '''
  Both the above tests pass, but function f1 has a bug! Write at least 5 test cases of your own for
  function f1 using testExact, and ensure that at least two of them fail.

  Your test cases cannot fail because you wrote the wrong expected value, the expected value you write
  must match the specification of the function. Your test cases must fail because they found the
  problem in f1 that causes it to not match the specification.

  That means, you cannot write a test case like this:
  testExact("f1_badTest", "xyz", f1, "abc", "x")
  Because that indicates that the function call f1("abc", "x") should
  produce the result "xyz", which is not correct as is meant to produce
  the reuslt "abc".
  '''

  # Place your test cases for f1 below this.


  # Now, about testing with testWithin and testing f2.
  '''
  testWithin is used to write test cases for functions whos return values cannot be tested
  for exact equality (in this class pretty much just floats).

  The first argument to provide to testWithin is a string which is the name of the test.
  The second argument to provide to testWithin is the expected value, that is the result
      you expect to be produced by the test case you are writing
  The third argument to provide to testWithin is the error threshold. That is how much
      in either direction you are willing to accept the return value of the function
      is off from the expected value.
  The fourth argument to provide to testWithin is the function that is to be tested in this
      test case.
  After the fourth argument, there should be a number of arguments equal to the number of
      parameters the function being tested has. The order of these arguments should also
      match the order of the parameters of the function being tested. These are the
      arguments to supply to that function for the given test case.

  Full documentation of testWithin is provided in the cmput274 module. It can be accessed
  by running the commands

  from cmput274 import *
  help(testWithin)

  in your Python shell.
  '''

  # Below means test f2(10) -> 3.1415926535897 ± 0.0001 to pass. It fails.
  testWithin("f2_test1", 3.1415926535897, 0.0001, f2, 10)
  # Below means test f2(15) -> 3.1415926535897 ± 0.0001 to pass. It fails.
  testWithin("f2_test2", 3.1415926535897, 0.0001, f2, 15)
  '''
  Write at least three more test cases for f2. All of them must use the value
  3.1415926535897 as the target and 0.0001 as the error. At least
  one of the test cases must pass.

  The argument provided for one of your passing test cases must be no more than
  20 away from a failing test case. That is, there should be at least one
  of your test cases where the argument you provide is X, and the test case
  passes, but X-20 fails.
  '''

  # Place your test cases for f2 below this.


  # The runTests function runs all tests that have been created.
  # It should be called only after all your test cases ahve already
  # been created with the appropriate function calls.
  runTests()


'''
This code below indicates that the main function
should execute when you ask the Python interpreter
to execute this Python file as a program. That is
done by executing the python interpreter command
and providing the path to this file as a command
line argument.

So, given that this program is named q2.py if your
shell is set to a current working directory
that contains this file, then you can run the
command

python3 q2.py

to run this program, which will run the main
function which then runs all the test cases.
'''
if __name__ == "__main__":
  main()
