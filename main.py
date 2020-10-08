from YALL import Lexer

prog = r"(\x. (\y. x + y))"

var = []
bes = []

lex = Lexer(prog)
while not lex.basic:
  lex = Lexer(lex.scanexpr())
  scan = Lexer(lex.text, "\\", ".")
  var.append(scan.scanexpr().strip())
  bes.append(scan.eatRest().strip())

print(var)
print(bes)