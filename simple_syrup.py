from typing import List, Union, TypeVar, Generator, Callable
from functools import reduce, partial

# basic function & typing
def add(x: int, y: int) -> int:
    return x + y

# declare, tuple
nums = (10, 100)

# tuple apply
it = add(*nums)

print(it) # 110
print(add(10, 200)) # 210

# typing types (List here), functools reduce
def add_stuff(items: List[int]) -> int:
    return reduce(add, items, 0)

print(add_stuff([1,2,3,4,5])) # 15

# lambda, map, list
map10 = map(lambda x: x + 10, [1,2,3,4,5])
print(list(map10)) # [11, 12, 13, 14, 15]

#sum
map10_2 = map(lambda x: x + 10, [1,2])
print(sum(map10_2)) # 23

# partial functions, generator expression (saves memory over using list comprehension)
add10 = partial(add, 10)

print(sum(add10(x) for x in [1,2,3,4])) # 50

# tree, functionaly, union typing, Generic types, recursive Type
# more on types in pylance https://devblogs.microsoft.com/python/pylance-introduces-five-new-features-that-enable-type-magic-for-python-developers/
A = TypeVar("A")

Tree = Union[tuple[A, "Tree", "Tree"], A]

# ConsList = Union[tuple[A, "ConsList"], None]

# first: ConsList[int] = (100, None)
# clist: ConsList[int] = (10, first)

# tree: Tree[int] = (10, (10), (10))

# def treeid() -> Tree[int]:
#     # return 10 # works
#     return (10, 1, 20)
    # return identity((10, (5, (3, 1, 2), (2, 1, 4)), (15, (14, 14, 12), (11, 18, 19))))

# generators, callables, lambdas
def lam(x: int) -> Callable[[int], Generator[int, None, None]]:
    return lambda start: (add10(y) for y in range(start, x))
