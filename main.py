from YALL import Lexer
from Machine import Machine, single, multi

# single.env = {"y": 6}
print(multi(5)(5))

# prog = r"(\x. (\y. x + y))"
# var = []
# bes = []
# lex = Lexer(prog)
# while not lex.basic:
#   lex = Lexer(lex.scanexpr())
#   scan = Lexer(lex.text, "\\", ".")
#   var.append(scan.scanexpr().strip())
#   bes.append(scan.eatRest().strip())
# print(var)
# print(bes)