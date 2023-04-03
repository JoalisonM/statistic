from typing import List

def moda(x: List[float]) -> List[float]:
  counts = Counter(x)
  max_count = max(counts.values())
  return [x_i for x_i, count in counts.items() if count == max_count]