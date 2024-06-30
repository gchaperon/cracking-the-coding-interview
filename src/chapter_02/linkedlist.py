from __future__ import annotations
import typing as tp
import types
import dataclasses

T = tp.TypeVar("T")


@dataclasses.dataclass
class Node(tp.Generic[T]):
    value: T
    next: Node[T] | None = None


def make_list(iterable: tp.Iterable[T]) -> Node[T] | None:
    anchor = types.SimpleNamespace(next=None)
    last: types.SimpleNamespace | Node = anchor
    for value in iterable:
        node = Node(value)
        last.next = node
        last = node
    return anchor.next
