class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.ast = []
        self.treepos = [0]
    def step(self):
        self.pos += 1
        return self.source[self.pos]
    def peek(self):
        return self.source[self.pos + 1]
    def stepUntilNotWhitespace(self):
        while self.source[self.pos] == ' ' or self.source[self.pos] == '\n' or self.source[self.pos] == '\t':
            self.pos += 1
    def createAst(self):
        try:
            while True:
                x = self.step()
                elif x == '(':
                    if x == '\\':
                        self.ast.append(['ab'])
                    else:
                        self.ast.append(x)
                elif x == ')':
                    pass
        except:
            return