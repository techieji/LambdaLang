# from YALL import Lexer
# from Machine import Machine
from scanner import ap, ab, eq

prog = r"fn1 = fn2 = (\x. (\y. (sub)(x)(y)))(5)(5)"
base = eq(prog)
appl = ap(base[-1])
abra = ab(appl[0])