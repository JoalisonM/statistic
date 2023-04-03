from estatistica.variancia import dot, de_media
from typing import List

def covariancia(xs: List[float], ys: List[float]) -> float:
  assert len(xs) == len(ys)

  return dot(de_media(xs), de_media(ys)) / (len(xs)-1)