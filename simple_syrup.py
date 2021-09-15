from typing import List, Union, TypeVar, Generator, Callable, Iterable
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


# generator expressions, callables, lambdas
def isEven(it: int) -> bool:
    return it % 2 == 0

def lam(start: int) -> Callable[[int], Generator[int, None, None]]:
    return lambda end: (add10(y) for y in range(start, end) if isEven(y))

print(list(lam(10)(20)))


# map and filter
def mapfilter(start: int, end: int) -> Iterable[int]: #Generator[int, None, None]:
    return map(add10, filter(isEven, range(start, end)))

print(list(mapfilter(10, 20)))


# loops and generators
def loopyrange(start: int, end: int) -> Generator[int, None, None]:
    for it in range(start, end):
        if (isEven(it)):
            yield add10(it)

print(list(loopyrange(10, 20)))

# tree, functionaly, union typing, Generic types, recursive Type
# more on types in pylance https://devblogs.microsoft.com/python/pylance-introduces-five-new-features-that-enable-type-magic-for-python-developers/
# for now, pylance (and others?) do not like recursive types with generics.
# recursive types are ok
# generics are ok
# both together does not seem to be
A = TypeVar("A")

Tree = Union[tuple[A, "Tree", "Tree"], A]

# ConsList = Union[tuple[A, "ConsList"], None]
ConsList = Union[tuple[int, "ConsList"], None]
# first: ConsList[int] = (100, None)
# clist: ConsList[int] = (10, first)
first: ConsList = (100, None)
clist: ConsList = (10, first)
# # tree: Tree[int] = (10, (10), (10))

# def treeid() -> Tree[int]:
#     # return 10 # works
#     return (10, 1, 20)
    # return identity((10, (5, (3, 1, 2), (2, 1, 4)), (15, (14, 14, 12), (11, 18, 19))))