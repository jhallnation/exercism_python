from typing import List

def slices(series: str, length: int) -> List[int]:
  if  length > len(series) or length < 1:
    raise ValueError("Invalid input")

  return [series[i:i+length] for i in range(0,len(series) - length + 1)]