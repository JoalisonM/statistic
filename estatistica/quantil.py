from typing import List
def quantil(xs: List[float], p:float) -> float:
  p_index = int(p * len(xs))
  return sorted(xs)[p_index]