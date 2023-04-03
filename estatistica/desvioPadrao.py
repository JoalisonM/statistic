import math
from typing import List
from estatistica.variancia import variancia

def desvio_padrao(xs: List[float])->float:
  """Desvio padrão ao é a raiz quadrada da variância"""
  return math.sqrt(variancia(xs))