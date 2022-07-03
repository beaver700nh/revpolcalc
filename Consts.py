import math

CONSTANTS = {
  "pi":  math.pi,
  "tau": math.tau,
  "e":   math.e,
}

def get(name):
  return CONSTANTS[name]
