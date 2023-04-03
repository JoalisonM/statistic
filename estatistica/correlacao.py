from typing import List
from estatistica.desvioPadrao import *
from estatistica.covariancia import *

def correlacao(xs: List[float], ys: List[float]) -> float:
  """Mede a variação simultânea de xs e ys a partir de duas médias"""
  stdev_x = desvio_padrao(xs)
  stdev_y = desvio_padrao(ys)
  if(stdev_x>0 and stdev_y>0):
    return covariancia(xs, ys) / stdev_x / stdev_y
  else:
    return 0