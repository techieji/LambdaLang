from YALL import Lexer
from Machine import Machine

def deparen(string):
  if string[0] == "(" and string[-1] == ")":
    return string[1:-1]
  return string

def ap(prog):
  lex = Lexer(prog)
  strs = [lex.scanexpr()]
  while strs[-1]:
    strs.append(lex.scanexpr())
  return strs[:-1]

def ab(prog):
  lex = Lexer(prog, start="\\", end=".")
  strs = [lex.scanexpr().strip(), deparen(lex.eatRest().strip())]
  return strs

def eq(prog):
  *vs, val = prog.split("=")
  vs = [x.strip() for x in vs]
  val = val.strip()
  return [vs, val]

def classifiy(string):
  if "=" in string:
    return eq

def abtoM(about):
  return Machine(
    about[0]
  )