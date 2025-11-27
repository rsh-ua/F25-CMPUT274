from cmput274 import *


def strToTokenList(s):
  '''
  strToTokenList takes a string that represents a valid fimpl program
                 and returns the sequential LList of tokens that
                 appear in that program.
  
  s       - str
  returns - LList of str

  Examples:
    strToTokenList("mul add -3 5 sub 1 -4 ") 
        -> LL("mul", "add", "-3", "5", "sub", "1", "-4")
    strToTokenList("add      -2\n\n   \t4") 
        -> LL("add", "-2", "4")
  '''
  pass


def isIdentifier(s):
  '''
  isIdentifier returns True if the given string is a valid fimpl
               identifier, False otherwise.

  s       - str
  returns - bool

  Examples:
    isIdentifier("foo") -> True
    isIdentifier("Foo") -> False
    isIdentifier("add") -> False
    isIdentifier("xDIM") -> True
  '''
  pass


'''
An ExprTree is one of:
 - LL("ident", str)
 - LL("intLit", int)
 - LL("binOp", Operator, ExprTree, ExprTree)

An Operator is one of:
 - "add"
 - "mul"
 - "div"
 - "sub"
'''

def tokensToExprTree(tokens):
  '''
  tokensToExprTree parses the first complete expression in the LList of tokens
                   into an ExprTree and returns a pair of the form
                   LL(ExprTree, LList) where the first item is the ExprTree
                   that represents the given expression, and the second item
                   is the parameter tokens but without any of the tokens that
                   were used to construct this expression

  tokens  - A LList of str
  returns - A LL(ExprTree, LList of Str)

  Examples:
    tokensToExprTree(LL("add", "-2", "4"))
      -> (('binOp',
           'add',
           ('intLit', -2),
           ('intLit', 4)),
         ())
    tokensToExprTree(LL("x", "5", "add", "3", "y"))
      -> (("ident", "x"),
          ("5", "add", "3", "y"))
    tokensToExprTree(LL("add", "x", "add", "5", "3", "mul", "10", "2"))
      -> (('binOp', 
           'add',
            ('ident', 'x'),
            ('binOp', 'add',
              ('intLit', 5),
              ('intLit', 3)
            )
          )
          ("mul", "10", "2")
         )
  '''
  pass

def lookup(key, pairs):
  '''
  lookup returns the value associated with the given key in the
         LList of pairs. May assume the key exists in the LList
         of pairs

  key     - X
  pairs   - LList of LL(X, Y)
  returns - Y

  Examples:
    lookup("x", LL(LL("x", 5), LL("y", 10))) -> 5
    lookup("y", LL(LL("x", 5), LL("y", 10))) -> 10
  '''
  pass


def evalExpr(eTree, defns):
  '''
  evalExpr returns the result of evaluating the given ExprTree eTree given
           the provided identifier definitions in the LList of pairs defns

  eTree   - an ExprTree
  defns   - a LList of LL(str, int)
  returns - int

  Examples:
    evalExpr(first(tokensToExprTree(strToTokenList("mul add -3 5 sub 1 -4 "))),
            LL()) -> 10

    evalExpr(first(tokensToExprTree(strToTokenList("add x 3"))),
            LL(LL("x", 2))) -> 5

    evalExpr(first(tokensToExprTree(strToTokenList("add x 3"))),
            LL(LL("x", -25))) -> -22
  '''
  pass


def main():
  testExact("tList1", LL("mul", "add", "-3", "5", "sub", "1", "-4"),
            strToTokenList, "mul add -3 5 sub 1 -4 ")
  testExact("tList2", LL("add", "-2", "4"),
            strToTokenList, "add      -2\n\n   \t4")

  testExact("isID1", True, isIdentifier, "foo")
  testExact("isID2", False, isIdentifier, "Foo")
  testExact("isID3", False, isIdentifier, "add")
  testExact("isID4", True, isIdentifier, "xDIM")

  testExact("exprTree1", 
            LL(LL('binOp',
                  'add',
                  LL('intLit', -2),
                  LL('intLit', 4)),
              LL()), 
            tokensToExprTree, 
            LL("add", "-2", "4"))

  testExact("exprTree2",
            LL(LL('binOp',
                  'add',
                  LL('ident', 'x'),
                  LL('binOp', 'add',
                     LL('intLit', 5),
                     LL('intLit', 3))),
                LL("mul", "10", "2")),
            tokensToExprTree,
            LL("add", "x", "add", "5", "3", "mul", "10", "2"))

  testExact("lookup1", 5, lookup, "x", LL(LL("a", 3), LL("x", 5)))

  
  fimplProg1 = "mul add -3 5 sub 1 -4 "
  genTree = lambda prog: first(tokensToExprTree(strToTokenList(prog)))
  testExact("eval1", 10, evalExpr,
            genTree(fimplProg1), empty())
  fimplProg2 = "add x 3"
  defns1 = LL(LL("x", 2))
  testExact("eval2", 5, evalExpr, 
            genTree(fimplProg2), defns1)

  defns2 = LL(LL("x", -25))
  testExact("eval2", -22, evalExpr, 
            genTree(fimplProg2), defns2)


  # Place your additional tests above here
  runTests()

if __name__ == "__main__":
  main()
