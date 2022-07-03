import Util

import math

def _add(stack):
  sum = stack[-2] + stack[-1]
  return Util.Result.OP, (sum, 2)

def _sub(stack):
  diff = stack[-2] - stack[-1]
  return Util.Result.OP, (diff, 2)

def _mul(stack):
  prod = stack[-2] * stack[-1]
  return Util.Result.OP, (prod, 2)

def _div(stack):
  op1 = stack[-2]
  op2 = stack[-1]

  if op2 == 0:
    print("Division by zero error!")
    return None

  return Util.Result.OP, (op1 / op2, 2)

def _mod(stack):
  rem = stack[-2] % stack[-1]
  return Util.Result.OP, (rem, 2)

def _neg(stack):
  return Util.Result.OP, (0 - stack[-1], 1)

def _pow(stack):
  res = stack[-2] ** stack[-1]
  return Util.Result.OP, (res, 2)

def _root(stack):
  op1 = stack[-1]
  op2 = (1.0 / stack[-2])

  if op1 < 0:
    print("Complex numbers are not supported. (sqrt of negative number)")
    return None

  return Util.Result.OP, (op1 ** op2, 2)

def _log(stack):
  operand = stack[-1]

  if operand <= 0:
    print("Can only calculate logarithm of positive numbers!")
    return None

  return Util.Result.OP, (math.log(operand), 1)

def _logn(stack):
  op1 = stack[-1]
  op2 = stack[-2]

  if op1 <= 0:
    print("Can only calculate logarithm of positive numbers!")
    return None

  return Util.Result.OP, (math.log(op1, op2), 2)

def _sin(stack):
  return Util.Result.OP, (math.sin(stack[-1]), 1)

def _cos(stack):
  angle = stack[-1]
  return Util.Result.OP, (math.cos(stack[-1]), 1)

def _tan(stack):
  angle = stack[-1]

  if angle == 0.5 * math.pi or angle == 1.5 * math.pi:
    print("tan() is undefined at 1/2 * PI and 3/2 * PI!")
    return None

  return Util.Result.OP, (math.tan(angle), 1)

def _asin(stack):
  sin_ = stack[-1]

  if sin_ < -1 or sin_ > 1:
    print("Input to asin() must be between -1 and 1!")
    return None

  return Util.Result.OP, (math.asin(sin_), 1)

def _acos(stack):
  cos_ = stack[-1]

  if cos_ < -1 or cos_ > 1:
    print("Input to acos() must be between -1 and 1!")
    return None

  return Util.Result.OP, (math.acos(cos_), 1)

def _atan(stack):
  return Util.Result.OP, (math.atan(stack[-1]), 1)

def _fact(stack):
  try:
    return Util.Result.OP, (math.factorial(stack[-1]), 1)
  except ValueError:
    print("Input to fact() must be a positive integer!")
    return None

def _help(stack):
  print(
    "--- RevPolCalc - Reverse Polish Calculator! ---",
    "+     Adds two numbers",
    "-     Subtracts two numbers",
    "*     Multiplies two numbers",
    "/     Divides two numbers",
    "%     Calculates remainder after dividing two numbers",
    "neg   Calculates the opposite of a number",
    "^     Raises first number to power of second number",
    "rt    (n x rt) Calculates nth root of x",
    "log   Calculates natural logarithm of a number",
    "logn  (b x rt) Calculates base b logarithm of x",
    "sin   Calculates sine of angle given in radians",
    "cos   Calculates cosine of angle given in radians",
    "tan   Calculates tangent of angle given in radians",
    "asin  Calculates the angle in radians whose sine is the number given",
    "acos  Calculates the angle in radians whose cosine is the number given",
    "atan  Calculates the angle in radians whose tangent is the number given",
    "fact  Calculates the factorial of a number",
    "help  Displays this help text",
    "=> Type Ctrl-C to quit. <=",
    sep="\n"
  )

  return Util.Result.OP, (0, 0)

OPERATIONS = {
  "+":    _add,
  "add":  _add,
  "-":    _sub,
  "sub":  _sub,
  "*":    _mul,
  "x":    _mul,
  "X":    _mul,
  "mul":  _mul,
  "/":    _div,
  "div":  _div,
  "%":    _mod,
  "mod":  _mod,
  "neg":  _neg,
  "opp":  _neg,
  "^":    _pow,
  "**":   _pow,
  "pow":  _pow,
  "rt":   _root,
  "root": _root,
  "log":  _log,
  "logn": _logn,
  "sin":  _sin,
  "cos":  _cos,
  "tan":  _tan,
  "asin": _asin,
  "acos": _acos,
  "atan": _atan,
  "!":    _fact,
  "fact": _fact,
  "help": _help,
}

def call(op, stack):
  return OPERATIONS[op](stack)
