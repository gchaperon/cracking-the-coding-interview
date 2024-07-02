from __future__ import annotations

import dataclasses
import typing as tp

T = tp.TypeVar("T")


@dataclasses.dataclass
class Node(tp.Generic[T]):
    value: T
    next: Node[T] | None = None


@dataclasses.dataclass
class Anchor(tp.Generic[T]):
    next: Node[T] | None = None


class HasNext(tp.Protocol, tp.Generic[T]):
    next: Node[T] | None


def make_list(iterable: tp.Iterable[T]) -> Node[T] | None:
    anchor: Anchor[T] = Anchor()
    last: HasNext[T] = anchor
    for value in iterable:
        node = Node(value)
        last.next = node
        last = node
    return anchor.next
