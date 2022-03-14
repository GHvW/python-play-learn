
from typing import Callable

from typing import TypeVar, Callable, Generic

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


class Compose(Generic[A, B]):

    def __init__(self, fn: Callable[[A], B]) -> None:
        self.fn = fn

    def __call__(self, x: A) -> B:
        return self.fn(x)

    def and_then(self, other: Callable[[B], C]) -> "Compose[A, C]":
        return Compose[A, C](lambda x: other(self.fn(x)))


def add10(x: int) -> int:
    return x + 10


def add100(x: int) -> int:
    return x + 100


print(Compose(add10).and_then(add100).and_then(add100)(1000))
