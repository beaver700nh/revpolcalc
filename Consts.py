import Util

import math

CONSTANTS = {
  "pi":  math.pi,
  "tau": math.tau,
  "e":   math.e,
}

def get(name):
  return Util.Result.VAL, CONSTANTS[name]
