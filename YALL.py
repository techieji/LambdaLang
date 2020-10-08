class Lexer:
  def __init__(self, text, start="(", end=")"):
    self.text = text
    self.pos = 0
    self.marks = []
    self.start = start
    self.end = end
    self.level = 0

  def eat(self):
    ret = self.text[self.pos]
  
    if ret == self.start:
      self.level += 1
    elif ret == self.end:
      self.level -= 1
  
    self.pos += 1
    return ret


  def cur(self):
    return self.text[self.pos]

  def peek(self):
    return self.text[self.pos + 1]

  def eatUntil(self, cond):
    while not cond(self.peek()):
      self.eat()

  def eatRest(self):
    ret = self.text[self.pos:]
    self.pos = len(self.text) - 1
    return ret

  def mark(self):
    self.marks.append(self.pos)

  def backtrack(self):
    self.pos = self.marks.pop()

  def scanexpr(self, revert=False):
    l = []
    while self.level <= 0:
      self.eat()
    if revert:
      self.mark()
    while self.level > 0:
      l.append(self.eat())
    if revert:
      self.backtrack()
    return "".join(l[:-1])

  @property
  def basic(self):
    if self.start in self.text or self.end in self.text:
      return False
    return True