from typing import List, Union, TypeVar, Generator, Callable, Iterable, Tuple
from functools import reduce, partial
from itertools import accumulate

# basic function & typing
def add(x: int, y: int) -> int:
    return x + y


# declare, tuple
nums = (10, 100)


# tuple apply
it = add(*nums)

print(it) # 110
print(add(10, 200)) # 210

# list apply
other_nums = [10, 100]
print(add(*other_nums))


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


# own higherorder and immediately invoke
def higherorder(it: Callable[[int, int], int]) -> Callable[[int], int]:
    return lambda x: it(x, 100)

print(higherorder(lambda x, y: x + y)(100000))


# conditional expression (ternary like functionality)
x = 40
cond_one = "less than 50" if x < 50 else "greater than or equal to 50"
cond_two = "less than 20" if x < 20 else "less than 30" if x < 30 else "greater than 29"

print(cond_one)
print(cond_two)


# itertools accumulate (like scan in Rx, rust, etc)
def accumulate_add10s(acc: int, next: int) -> int:
    return acc + add10(next)


acc_result: List[int] = list(accumulate([10, 20, 30], accumulate_add10s, initial=0))

athing = list(accumulate([1,2,3], initial=0))

print(acc_result)


# tree, functionaly, union typing, Generic types, recursive Type
# more on types in pylance https://devblogs.microsoft.com/python/pylance-introduces-five-new-features-that-enable-type-magic-for-python-developers/
# for now, pylance (and others?) do not like recursive types with generics.
# recursive types are ok
# generics are ok
# both together does not seem to be
A = TypeVar("A")

Tree = Union[Tuple[A, "Tree", "Tree"], A]

# ConsList = Union[tuple[A, "ConsList"], None]
ConsList = Union[Tuple[int, "ConsList"], None]
# first: ConsList[int] = (100, None)
# clist: ConsList[int] = (10, first)
first: ConsList = (100, None)
clist: ConsList = (10, first)
# # tree: Tree[int] = (10, (10), (10))

# def treeid() -> Tree[int]:
#     # return 10 # works
#     return (10, 1, 20)
    # return identity((10, (5, (3, 1, 2), (2, 1, 4)), (15, (14, 14, 12), (11, 18, 19))))