f = open("File.txt")
program = f.read()

def parsexpr(expr):
    term = []
    for x in range(0, len(expr)):
        if expr[x] == "/":
            term.append('ab')
            var = ""
            for i in range(x, len(expr) - 1):
                if expr[i] == ".":
                    term.append(["var", var, var])
                    term.append(parsexpr(expr[(i): (len(expr) - 1)]))
                    return term
                else:
                    var += expr[x + i]
        elif expr[x] == "(":
            term.append('ap')
            var = ""
            arg = ""
            flag = false
            for i in range(x, len(expr) - 1):
                if expr[i] == ")":
                    flag = True
                elif flag:
                    if expr[i] == ")":
                        
                        flag = False
                    else:
                        arg += i
                else:
                    var += i
    return term
