class Lexer:
    def __init__(self, source, identifiers):
        self.source = source
        self.pos = 0
        self.identifiers = identifiers
    def Eat(self): # returns the next character and advances the stream
        self.pos += 1
        return self.source[self.pos]
    def Peek(self): # returns the next character without advancing the stream
        return self.source[self.pos + 1]
    def EatWhitespace(self): # advances the stream until the next character isn't whitespace
        while self.Peek() == " " or self.Peek() == "\t" or self.Peek() == "\n":
            self.Eat()
    def EatUntilWhitespace(self): # returns the next word and advances the stream
        self.EatWhitespace()
        food = ""
        while self.Peek() != " " or self.Peek() != "\t" or self.Peek() != "\n":
            food += self.Eat()
        return food
    def EatAlpha(self):
        word = self.EatUntilWhitespace()
        flag = True
        for x in word:
            if not (x > 'a' and x < 'z') or (x > 'A' or x < 'Z'):
                flag = False
                break
        if flag:
            return word
    def EatNum(self):
        word = self.EatUntilWhitespace()
        try:
            return int(word)
        except ValueError:
            return
    def EatIdentifier(self):
        possibleid = self.EatAlpha()
        if not possibleid:
            return
        if possibleid in self.identifiers:
            return possibleid

#%%

def match(fulltext: str, subtext: str) -> int:
    for x in range(0, len(fulltext) - len(subtext)):
        if fulltext[x:(x + len(subtext))] == subtext:
            return x
    return -1

class Syntax:
    def __init__(self, identifier: str, value: str, function):
        self.identifier = identifier
        self.value = value
        self.function = function
    def exec(self, code):
        rawparts = self.value.split('!')
        parts = rawparts[0:len(rawparts):2]
        args = []
        for x in range(0, len(parts) - 1):
            rawargs = code[match(code, parts[x]) + len(parts[x]):match(code, parts[x + 1])]
            args.append(rawargs)
        return self.function(*args)
    def nestedexec(self, code):
        rawparts = self.value.split('!')
        parts = rawparts[0:len(rawparts):2]
        rawargs = []
        args = []
        for x in range(0, len(parts) - 1):
            rawargs.append(code[match(code, parts[x]) + len(parts[x]):match(code, parts[x + 1])])
        rawargs[-1] += self.value[-1]
        for x in rawargs:
            args.append(run(x))
        return self.function(*args)
    def isSyntax(self, code):
        rawparts = self.value.split('!')
        parts = rawparts[0:len(rawparts):2]
        firstpart = parts[0]
        if match(code, firstpart) == -1:
            return False
        return True

class BaseSyntax(Syntax):
    def __init__(self, identifier, value, function):
        super().__init__(identifier, value, function)
    def nestedexec(self, code):
        rawparts = self.value.split('!')
        parts = rawparts[0:len(rawparts):2]
        rawargs = []
        args = []
        for x in range(0, len(parts) - 1):
            rawargs.append(code[match(code, parts[x]) + len(parts[x]):match(code, parts[x + 1])])
        rawargs[-1] += self.value[-1]
        return self.function(*rawargs)

syntaxes = (
    Syntax('write', "write <!0!>", lambda x: print(x)),
    Syntax('add', "add <!0! + !1!>", lambda x, y: x + y),
    BaseSyntax('str', "'!0!'", lambda x: str(x)),
    BaseSyntax('str', '"!0!"', lambda x: str(x)),
)

atom = Syntax('atom', '!0!', lambda x: x)

def matchSyntax(code: str) -> Syntax:
    for x in syntaxes:
        if x.isSyntax(code):
            return x
    return atom

def oldrun(code):
    for x in syntaxes:
        if x.isSyntax(code):
            return x.exec(code)
            break

def run(code: str):
    firstsyntax = matchSyntax(code)
    return firstsyntax.nestedexec(code)

code = "write <add <1 + 2>>"

while True:
    code = input('> ')
    print(run(code))