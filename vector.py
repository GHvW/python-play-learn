from typing import List, Tuple
# from collections import namedtuple


def scale(scalar: float, vec: List[float]) -> List[float]:
    return [(item * scalar) for item in vec]

def addvecs(first: List[float], second: List[float]) -> List[float]:
    return [x + y for x, y in zip(first, second)]

def addVec2s(first: Tuple[float, float], second: Tuple[float, float]) -> Tuple[float, float]:
    return (first[0] + second[0], first[1] + second[1])
