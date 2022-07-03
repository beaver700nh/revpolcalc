import Ops
import Consts
import Util

def isnumber(s):
  try:
    float(s)
  except ValueError:
    return False
  else:
    return True

def operation(tok, stack):
  try:
    return Ops.call(tok, stack)
  except KeyError:
    print(f"No such operator '{tok}'!")
    return None

def constant(name):
  if name == "":
    print("Unnamed constant!")
    return None

  try:
    return Consts.get(name)
  except KeyError:
    print(f"Unknown constant '{name}'!")
    return None

def handle(tok, stack):
  if isnumber(tok):
    return Util.Result.VAL, float(tok)

  elif tok.startswith("$"):
    return constant(tok[1:])

  else:
    return operation(tok, stack)

def evaluate(expr):
  tokens = [t for t in expr.split(" ") if t]

  if not tokens:
    print("Nothing to evaluate!")
    return None

  stack = []

  for tok in tokens:
    tok = tok.strip()
    returned = handle(tok, stack)

    if returned is None: break

    type, result = returned

    if type == Util.Result.VAL:
      stack.append(result)

    elif type == Util.Result.OP:
      if len(stack) == 0 and tok != "help":
        print("There are no operands to be operated on!")
        break

      value, popped = result

      if popped > len(stack):
        print(f"Operator '{tok}' requires {popped} operands but got only {len(stack)}!")
        break

      for _ in range(popped): stack.pop()
      stack.append(value)

  else:
    if len(stack) > 1:
      print(f"Warning: Leftover operands without any operators!")

    return stack.pop()

  return "[Error.]"

while True:
  try:
    expr = input(": ")
  except KeyboardInterrupt:
    print("\n[Quit.]")
    break

  print(f"=> {evaluate(expr)}\n")
