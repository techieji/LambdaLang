stacks = {
  "ADD": lambda s: s.append(s.pop() + s.pop()),
  "SUB": lambda s: s.append(s.pop() - s.pop()),
  "OUT": lambda s: print(s.pop()),
  "POW": lambda s: pow(s.pop(), s.pop())
}

envs = {
  "CONST": lambda s, a: s.append(a[0]),
  "CONSTPOW": lambda s, a: s.append(pow(s.pop(), a)),
  "PYFUNC": lambda s, a: s.append(a(s))
}

class Machine:
  def __init__(self, var, code, env={}):
    self.var = var
    self.code = code
    self.env = env
    self.val = None
  
  def __call__(self, val, env={}):
    wk = self.substitute(self.var, val)
    self.env[self.var] = val
    for var, val in {**env, **self.env}.items():
      wk = Machine(var, wk).substitute(var, val)
      self.env[var] = val
    return Machine.run(Machine("quaint", wk))

  def substitute(self, var, val):
    newcode = []
    self.val = val
    for kw, *rest in self.code:
      if kw == "LOAD" and rest[0] == var:
        newcode.append(("CONST", val))
      else:
        newcode.append((kw, *rest))
    return newcode

  def run(machine, env={}):
    code = machine.code
    # print(code)
    s = []
    for kw, *a in code:
      # print(kw)
      if kw == "STACK":
        stacks[a[0]](s)
      elif kw in envs:
        envs[kw](s, a)
      elif kw == "RUNMACHINE":
        a[0].env = machine.env
        s.append(
          a[0]
        )
      elif kw == "RETURN":
        return s.pop()

single = Machine(
  "x",
  [("LOAD", "x"), 
  ("LOAD", "y"), 
  ("STACK", "ADD"), 
  ("STACK", "OUT")]
)

multi = Machine(
  "x",
  [("RUNMACHINE", Machine(
    "y",
    [("LOAD", "x"), 
    ("LOAD", "y"), 
    ("STACK", "ADD"), 
    ("RETURN",)]
  )),
  ("RETURN",)]
)