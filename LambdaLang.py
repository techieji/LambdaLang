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
        elif expr[x] == "(":
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

def runsnippet(snippet):
    functions = {
        "write": ((1), lambda x: print(x[0])),
        "+": ((-1, 1), lambda x: int(x[0]) + int(x[1]))
    }

    def parse(string):
        lis = []
        word = ""
        for x in string:
            if x == " ":
                lis.append(word)
                word = ""
            else:
                word += x
        lis.append(word)
        return lis

    function = ""
    code = parse(snippet)
    for x in functions:
        if x in code:
            function = x
            break
    
    args = []
    indexes = functions[function][0]
    if type(indexes) != tuple:
        indexes = (indexes)
    for x in indexes:
        args.append(code[code.index(function) + x])

    return functions[function][1](args)
    return NotImplemented

def findsnippets(lis):
    snippets = []
    for x in range(0, len(lis)):
        try:
            if type(lis[x]) == list:
                snippets.append((x ,findsnippets(lis[x])))
            elif runsnippet(lis[x]) != NotImplemented:
                snippets.append((x, lis[x]))
        except:
            continue
    return snippets

print(findsnippets(parsexpr(program)))