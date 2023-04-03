from typing import List
from estatistica.media import media

Vector = List[float]
def dot(v: Vector, w:Vector)->float:
  """Calcula o produtor escalar dos vetores"""
  assert len(v) == len(w)
  return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v: Vector)->float:
  """Retorna v_1*v_1 + ... v_n*v_n"""
  return dot(v, v)

def de_media(xs: List[float])->List[float]:
  x_bar = media(xs)
  return [x - x_bar for x in xs]

def variancia(xs: List[float])->float:
  assert len(xs) >= 2
  n = len(xs)
  desvios = de_media(xs)
  return sum_of_squares(desvios) / (n -1)