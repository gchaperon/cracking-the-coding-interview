from __future__ import annotations

import collections.abc
import dataclasses
import typing as tp

from graphs import Node

T = tp.TypeVar("T")
U = tp.TypeVar("U")


class llist(collections.abc.Iterable[T], tp.Generic[T]):
    @dataclasses.dataclass
    class Node(tp.Generic[U]):
        value: U
        next: llist.Node[U] | None = None

    _root: llist.Node[T] | None

    def __init__(self, iterable: tp.Reversible[T] = ()) -> None:
        self._root = None

        for element in reversed(iterable):
            self.appendleft(element)

    @classmethod
    def fromroot(self, root: llist.Node[T] | None) -> llist[T]:
        new: llist[T] = llist()
        new._root = root
        return new

    @classmethod
    def fromother(self, other: llist[T]) -> llist[T]:
        new: llist[T] = llist()
        new._root = other._root
        return new

    @property
    def head(self) -> T:
        if self._root is None:
            raise ValueError("llist is empty")
        return self._root.value

    @property
    def tail(self) -> llist[T]:
        if self._root is None:
            raise ValueError("llist is empty")
        return llist.fromroot(self._root.next)

    def appendleft(self, value: T) -> llist[T]:
        old_root = self._root
        self._root = llist.Node(value, old_root)
        return llist.fromroot(self._root)

    def __iter__(self) -> tp.Iterator[T]:
        pointer = self._root
        while pointer is not None:
            yield pointer.value
            pointer = pointer.next

    def __bool__(self) -> bool:
        return self._root is not None

    def __repr__(self) -> str:
        return "(" + " -> ".join(map(str, self)) + ")"


def interleaves(left: llist[int], right: llist[int]) -> tp.Iterable[llist[int]]:
    if not left:
        yield llist.fromother(right)
    elif not right:
        yield llist.fromother(left)
    else:
        yield from (
            interleave.appendleft(left.head)
            for interleave in interleaves(left.tail, right)
        )
        yield from (
            interleave.appendleft(right.head)
            for interleave in interleaves(left, right.tail)
        )


def bst_sequences(tree: Node[int] | None) -> set[tuple[int, ...]]:
    def impl(tree: Node[int] | None) -> tp.Iterable[llist[int]]:
        if tree is None:
            yield llist()
        else:
            yield from (
                interleave.appendleft(tree.value)
                for left_bst_sequence in impl(tree.left)
                for right_bst_sequence in impl(tree.right)
                for interleave in interleaves(left_bst_sequence, right_bst_sequence)
            )

    return {tuple(sequence) for sequence in impl(tree)}


# ******************** Tests ********************
def test_interleaves() -> None:
    def freeze(iterable: tp.Iterable[llist[int]]) -> set[tuple[int, ...]]:
        return {tuple(value) for value in iterable}

    assert freeze(interleaves(llist([]), llist([]))) == {tuple()}
    assert freeze(interleaves(llist([0]), llist([]))) == {(0,)}
    assert freeze(interleaves(llist([]), llist([1]))) == {(1,)}

    assert freeze(interleaves(llist([0]), llist([1]))) == {(0, 1), (1, 0)}


def test_bst_sequence() -> None:
    assert bst_sequences(None) == {tuple()}
    assert bst_sequences(Node(1)) == {(1,)}
    assert bst_sequences(Node(2, Node(1), Node(3))) == {(2, 1, 3), (2, 3, 1)}

    # NOTE: see assets/ch04_q09.svg, examples below correspond to that tree or
    # some subset of its nodes
    assert bst_sequences(
        Node(
            3,
            Node(
                2,
                Node(1),
            ),
            Node(5),
        )
    ) == {(3, 2, 1, 5), (3, 2, 5, 1), (3, 5, 2, 1)}

    assert bst_sequences(
        Node(
            3,
            Node(
                2,
                Node(1),
            ),
            Node(
                5,
                None,
                Node(7),
            ),
        )
    ) == {
        (3, 2, 1, 5, 7),
        (3, 2, 5, 1, 7),
        (3, 2, 5, 7, 1),
        (3, 5, 2, 1, 7),
        (3, 5, 2, 7, 1),
        (3, 5, 7, 2, 1),
    }

    assert bst_sequences(
        Node(
            3,
            Node(
                2,
                Node(1),
            ),
            Node(
                5,
                Node(4),
                Node(7),
            ),
        )
    ) == {
        (3, 2, 1, 5, 4, 7),
        (3, 2, 5, 1, 4, 7),
        (3, 2, 5, 4, 1, 7),
        (3, 2, 5, 4, 7, 1),
        (3, 5, 2, 1, 4, 7),
        (3, 5, 2, 4, 1, 7),
        (3, 5, 2, 4, 7, 1),
        (3, 5, 4, 2, 1, 7),
        (3, 5, 4, 2, 7, 1),
        (3, 5, 4, 7, 2, 1),
        (3, 2, 1, 5, 7, 4),
        (3, 2, 5, 1, 7, 4),
        (3, 2, 5, 7, 1, 4),
        (3, 2, 5, 7, 4, 1),
        (3, 5, 2, 1, 7, 4),
        (3, 5, 2, 7, 1, 4),
        (3, 5, 2, 7, 4, 1),
        (3, 5, 7, 2, 1, 4),
        (3, 5, 7, 2, 4, 1),
        (3, 5, 7, 4, 2, 1),
    }
