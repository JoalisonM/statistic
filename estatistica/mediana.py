from typing import List

def _med_impar(xs: List[float]) -> float:
  return sorted(xs)[len(xs) // 2]

def _med_par(xs: List[float]) -> float:
  sorted_xs = sorted(xs)
  meio_hi = len(xs) // 2
  return (sorted_xs[meio_hi-1] + sorted_xs[meio_hi]) / 2

def mediana(v: List[float]) ->float:
  return _med_par(v) if len(v) % 2 == 0 else _med_impar(v)