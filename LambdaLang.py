filename = "TestFile.ll"         #input("Enter a file: ")
f = open(filename)
program = f.read()

def parsexpr(expr): # this entire thing consists of hackish things.
    term = []
    for x in range(0, len(expr) - 1):
        if expr[x] == "\\":
            term.append('ab')
            var = ""
            for i in range(x, len(expr) - 1):
                if expr[i] == ".":
                    term.append(["var", var[1:], var[1:]])
                    term.append(parsexpr(expr[(i + 2):]))
                    return term
                else:
                    var += expr[x + i]
        elif expr[x] == "(": # need to implement resursiveness and IT NEEDS TO WORK PROPERLY!!!!!!!!!!
            term.append('ap')
            var = ""
            arg = ""
            flag = False
            flag2 = False
            for i in range(x, len(expr)):
                if expr[i] == ")" and not flag:
                    var += expr[i]
                    flag = True
                if flag:
                    arg += expr[i]
                    if expr[i] == ")":
                        if not flag2:
                            flag2 = True
                        elif flag2:
                            term.append(parsexpr(arg[2:len(arg) - 1]))    #term.append(parsexpr(arg[1:]))
                            term.append(parsexpr(var[1:len(var) - 1]))    #term.append(parsexpr(var))
                else:
                    var += expr[i]
            return term
    return [expr]

print(parsexpr(program))