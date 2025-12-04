from cmput274 import *

'''
A StmtTree is one of:
- LL("assign", ExprTree, ExprTree)
- LL("display", ExprTree)
- LL("repeat", ExprTree, LList of StmtTree)
'''

def replaceOrAdd(defns, key, val):
  pass

def tokensToStmtTree(tokens):
  '''
  tokensToStmtTree takes a LList of tokens and builds a StmtTree that represents the
                   first statement seen in tokens. It returns a LL(StmtTree, LList of str)
                   where the first item in the pair is the produced StmtTree and the 
                   second item in the pair is the remaining tokens.

  tokens  - LList of str, which represents tokens of a valid fimpl program
  returns - LL(StmtTree, LList of str)

  Side Effects: None

  Examples: 
    prog1 = "x <- 5\nDisp x\n x <- add x 1" 
    tokensToStmtTree(strToTokenList(prog1))
     -> (('assign', ('ident', 'x'), ('intLit', 5)), 
         ('Disp', 'x', 'x', '<-', 'add', 'x', '1'))
    
    prog2 = "Rpt x {\n y <- sub y 1\nDisp y\n}\nx <- add x 1"
    tokensToStmtTree(strToTokenList(prog2))
      -> (('repeat', 
            ('ident', 'x'), 
            (('assign', ('ident', 'y'), 
                        ('binOp', 'sub', 
                                  ('ident', 'y'), 
                                  ('intLit', 1))), 
              ('display', ('ident', 'y')))), 
          ('x', '<-', 'add', 'x', '1'))
      
  '''
  pass

def tokensToSTreeList(tokens):
  '''
  tokensToSTreeList takens a LList of tokens and returns a LList of StmtTree
                    that is the result of parsing all of the tokens into 
                    statements

  tokens  - LList of str, which represents tokens of a valid fimpl program
  returns - LList of StmtTree

  Side Effects: None

  Example:
    prog1 = "x <- 5\nDisp x\n x <- add x 1" 
    tokensToSTreeList(strToTokenList(prog1))
     -> (('assign', ('ident', 'x'), ('intLit', 5)), 
         ('display', ('ident', 'x')), 
         ('assign', ('ident', 'x'), ('binOp', 'add', ('ident', 'x'), ('intLit', 1))))
  '''
  pass
  

def runStmt(stmt, defns):
  '''
  runStmt takes a single StmtTree and a LList of pairs that
          represent identifier definitions and executes the
          given statement, returning an updated definitions LList
          and, if necessary, printing a value to the screen

  stmt    - a StmtTree, the statement to execute
  defns   - LList of LL(str, int), the identifier definitions
  returns - LList of LL(str, int), the updated identifier definitions

  Side Effects: May print to the screen

  Examples:
    stmt0 = first(tokensToSTreeList(strToTokenList("x <- 3")))
    runStmt(stmt1, empty()) -> LL(LL("x", 3))

    stmt1 = first(tokensToSTreeList(strToTokenList("x <- add x 1")))
    runStmt(stmt1, LL(LL("x", 3))) -> LL(LL("x", 4))

    stmt2 = first(tokensToSTreeList(strToTokenList("Disp sub x y")))
    runStmt(stmt2, LL(LL("x", 2), LL("y", 7))) -> LL(LL("x", 2), LL("y", 7))
    # Side effect: prints "-5\n" to the screen

    stmt3 = first(tokensToSTreeList(strToTokenList("Rpt 5 {\nx <- mul x 2\n}")))
    runStmt(stmt3, LL(LL("x", 2))) -> LL(LL("x", 64))
  '''
  pass

def interp(text):
  '''
  interp is our fimpl interpreter. It takes a single string parameter that
         is a valid fimpl program and executes that program

  text    - str, a valid fimpl program
  returns - None

  Examples:
    interp("x <- 1\nRpt 5 {\nDisp x\nx <- mul x 2\n}") -> None
      # Prints to the screen "1\n2\n4\n8\n16"
  '''
  pass


def testMain():
  testExact("replaceT1", LL(LL("y", 3), LL("x", 5)), replaceOrAdd, LL(LL("y", 3)), "x", 5)
  testExact("replaceT2", LL(LL("y", 17), LL("x", 5)), replaceOrAdd, LL(LL("y", 3), LL("x", 5)), "y", 17)

  prog1 = "x <- 5\nDisp x\n x <- add x 1"
  result1 = LL(LL('assign', LL('ident', 'x'), LL('intLit', 5)), LL('Disp', 'x', 'x', '<-', 'add', 'x', '1')) 
  testExact("tokensToStmtTreeT1", result1, tokensToStmtTree, strToTokenList(prog1))

  prog2 = "Rpt x {\n y <- sub y 1\nDisp y\n}\nx <- add x 1"
  result2 = LL(LL('repeat', 
                  LL('ident', 'x'), 
                   LL(LL('assign', 
                        LL('ident', 'y'), 
                        LL('binOp', 'sub', 
                            LL('ident', 'y'), 
                            LL('intLit', 1))), 
                  LL('display', LL('ident', 'y')))), 
            LL('x', '<-', 'add', 'x', '1'))
  testExact("tokensToStmtTreeT2", result2, tokensToStmtTree, strToTokenList(prog2))


  prog3 = "x <- 5\nDisp x\n x <- add x 1" 
  result3 = LL(LL('assign', 
                  LL('ident', 'x'), 
                  LL('intLit', 5)), 
              LL('display', 
                  LL('ident', 'x')), 
              LL('assign', 
                  LL('ident', 'x'), 
                  LL('binOp', 'add', 
                    LL('ident', 'x'), 
                    LL('intLit', 1))))
  testExact("stmtListT1", result3, tokensToSTreeList, strToTokenList(prog3))


  stmt0 = first(tokensToSTreeList(strToTokenList("x <- 3")))
  testExact("runStmtT0", LL(LL("x", 3)), runStmt, stmt0, empty())


  stmt1 = first(tokensToSTreeList(strToTokenList("x <- add x 1")))
  testExact("runStmtT1", LL(LL("x", 4)), runStmt, stmt1, LL(LL("x", 3)))

  stmt2 = first(tokensToSTreeList(strToTokenList("Disp sub x y")))
  # When a function has a return value and side effect of printing to the screen
  # we must test both
  # We have a new test function testPrint.
  # It works just like testExact except intead of expected being the value the function
  # should return, expected should be the string that the function call should print
  # to the screen.
  testExact("runStmtT2", LL(LL("x", 2), LL("y", 7)), runStmt, stmt2, LL(LL("x", 2), LL("y", 7)))
  testPrint("runStmtT2Print", "-5\n", runStmt, stmt2, LL(LL("x", 2), LL("y", 7)))

  stmt3 = first(tokensToSTreeList(strToTokenList("Rpt 5 {\nx <- mul x 2\n}")))
  testExact("runStmtT3", LL(LL("x", 64)), runStmt, stmt3, LL(LL("x", 2)))


  fullProg = "x <- 1\nRpt 5 {\nDisp x\nx <- mul x 2\n}"
  testPrint("interpT1", "1\n2\n4\n8\n16\n", interp, fullProg)


  runTests()

def main():
  '''
  Our main function is a bit different this time. When this program is executed it will ask for input from the
  user (you). You must enter either just the word tests if you would like to run the tests defined above (where you should
  also write your own tests), or you should enter the name of a plaintext file that contains a fimpl program that is
  stored in the same directory as your python program (or provide the path to a fimpl program if it resides elsewhere).

  This allows you to execute full fimpl programs easily by writing them in text files and providing them as the input when
  this program asks. It also will allow you to try the sample fimpl programs provided with the assignment once your
  interpreter is complete!
  '''
  choice = input("Enter the filename of the fimpl program you'd like to run or tests if you'd like to run the defined test cases: ")
  if choice != "tests":
    f = open(choice, "r")
    text = f.read()
    f.close()
    interp(text)
  else:
    testMain()


if __name__ == "__main__":
  main()
