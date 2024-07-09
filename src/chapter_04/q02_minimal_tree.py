from __future__ import annotations

import dataclasses
import itertools
import typing as tp

T = tp.TypeVar("T")


@dataclasses.dataclass
class Node(tp.Generic[T]):
    value: T
    left: Node[T] | None = None
    right: Node[T] | None = None


def height(tree: Node[int] | None) -> int:
    return 0 if tree is None else 1 + max(height(tree.left), height(tree.right))


def traverse_inorder(tree: Node[int] | None) -> list[int]:
    def traverse(tree: Node[int] | None) -> tp.Iterable[int]:
        if tree is not None:
            yield from itertools.chain(
                traverse(tree.left), [tree.value], traverse(tree.right)
            )

    return list(traverse(tree))


def minimal_tree(array: list[int]) -> Node[int] | None:
    n = len(array)
    if n == 0:
        return None
    else:
        half = n // 2
        return Node(
            array[half],
            minimal_tree(array[:half]),
            minimal_tree(array[half + 1 :]),
        )


# ******************** Tests ********************
def test_height() -> None:
    assert height(None) == 0
    assert height(Node(3)) == 1
    assert height(Node(1, Node(2))) == 2
    assert height(Node(1, None, Node(3, None, Node(4, None, Node(5))))) == 4


def test_traverse_in_order() -> None:
    assert traverse_inorder(None) == []
    assert traverse_inorder(Node(1)) == [1]
    assert traverse_inorder(Node(1, Node(2))) == [2, 1]
    assert traverse_inorder(Node(1, None, Node(2))) == [1, 2]
    assert traverse_inorder(
        Node(
            1,
            Node(
                2,
                Node(3, Node(4), Node(5)),
                Node(6, Node(7), Node(8)),
            ),
            Node(9, Node(10)),
        )
    ) == [4, 3, 5, 2, 7, 6, 8, 1, 10, 9]


def test_minimal_tree() -> None:
    import math
    import random

    rng = random.Random(123)
    for length in rng.sample(range(10, 30), k=10):
        array = sorted(rng.sample(range(100), k=length))
        tree = minimal_tree(array)
        assert traverse_inorder(tree) == array
        assert height(tree) == math.ceil(math.log2(length + 1))
