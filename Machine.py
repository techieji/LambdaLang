stacks = {
  "ADD": lambda s: s.append(s.pop() + s.pop()),
  "OUT": lambda s: print(s.pop())
}

envs = {
  "CONST": lambda s, a: s.append(a[0])
}

class Machine:
  def __init__(self, var, code, env={}):
    self.var = var
    self.code = code
    self.env = env
  
  def __call__(self, val, env={}):
    wk = self.substitute(self.var, val)
    for var, val in {**env, **self.env}.items():
      wk = Machine(var, wk).substitute(var, val)
    return Machine.run(Machine("quaint", wk))

  def substitute(self, var, val):
    newcode = []
    for kw, a, *rest in self.code:
      if kw == "LOAD" and a == var:
        newcode.append(("CONST", val))
      else:
        newcode.append((kw, a, *rest))
    return newcode

  def run(machine, env={}):  # Note that this is basic; it doesn't support RUNMACHINE
    code = machine.code
    s = []
    for kw, *a in code:
      if kw == "STACK":
        # print("stacks")
        stacks[a[0]](s)
      elif kw in envs:
        # print("envs")
        envs[kw](s, a)
      elif kw == "RUNMACHINE":
        a[0].env = dict(env)
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
    ("RETURN")]
  )),
  ("RETURN")]
)