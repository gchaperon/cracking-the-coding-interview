from __future__ import annotations
import typing as tp
import types
import dataclasses

T = tp.TypeVar("T")


@dataclasses.dataclass
class Node(tp.Generic[T]):
    value: T
    next: Node[T] | None = None


class _HasNext(tp.Protocol, tp.Generic[T]):
    next: Node[T] | None


def make_list(iterable: tp.Iterable[T]) -> Node[T] | None:
    anchor: _HasNext[T] = types.SimpleNamespace(next=None)
    last = anchor
    for value in iterable:
        node = Node(value)
        last.next = node
        last = node
    return anchor.next
