from __future__ import annotations

import collections
import dataclasses
import itertools
import random
import typing as tp

import pytest


@dataclasses.dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None
    size: int = 1


def traverse_children(node: Node | None) -> tp.Iterable[Node]:
    if node is not None:
        yield from itertools.chain(
            [node],
            traverse_children(node.left),
            traverse_children(node.right),
        )


@dataclasses.dataclass
class Tree:
    _root: Node | None = None

    def insert(self, value: int) -> None:
        def insert_impl(root: Node | None, value: int) -> Node:
            if root is None:
                return Node(value)
            elif value < root.value:
                return dataclasses.replace(
                    root,
                    left=insert_impl(root.left, value),
                    size=root.size + 1,
                )
            else:
                return dataclasses.replace(
                    root,
                    right=insert_impl(root.right, value),
                    size=root.size + 1,
                )

        self._root = insert_impl(self._root, value)

    def find(self, value: int) -> Node | None:
        def find_impl(node: Node | None, value: int) -> Node | None:
            if node is None:
                return None
            elif node.value == value:
                return node
            else:
                return find_impl(node.left, value) or find_impl(node.right, value)

        return find_impl(self._root, value)

    def delete(self, value: int) -> None:
        def delete_impl(
            node: Node | None, value: int
        ) -> tuple[Node | None, Node | None]:
            if node is None:
                return None, None
            elif node.value == value:
                return None, node
            else:
                newleft, dleft = delete_impl(node.left, value)
                newright, dright = delete_impl(node.right, value)
                removed = dleft or dright
                return (
                    dataclasses.replace(
                        node,
                        left=newleft,
                        right=newright,
                        size=node.size - removed.size if removed else node.size,
                    ),
                    removed,
                )

        self._root, removed = delete_impl(self._root, value)
        for child in itertools.islice(traverse_children(removed), 1, None):
            self.insert(child.value)

    def __len__(self) -> int:
        return self._root.size if self._root else 0

    def get_random_node(self, rng: random.Random | None = None) -> Node:
        if len(self) == 0:
            raise ValueError("Cannot get random node from empty tree")

        rng = rng or random.Random()

        def random_impl(node: Node | None) -> Node:
            assert node is not None
            left_count = node.left.size if node.left else 0
            right_count = node.right.size if node.right else 0
            p, *_ = rng.sample([1, 2, 3], k=1, counts=[1, left_count, right_count])
            if p == 1:
                return node
            elif p == 2:
                return random_impl(node.left)
            elif p == 3:
                return random_impl(node.right)
            else:
                raise ValueError

        return random_impl(self._root)


# ******************** Tests ********************
def test_insert() -> None:
    tree = Tree()
    assert len(tree) == 0

    rng = random.Random(123)
    n = 20
    for i in rng.sample(range(-50, 50), k=n):
        tree.insert(i)

    assert len(tree) == n


def test_delete() -> None:
    tree = Tree()
    assert len(tree) == 0

    for i in range(10):
        tree.insert(i)

    assert len(tree) == 10

    for i in range(5):
        tree.delete(i)
    assert len(tree) == 5

    for i in range(5, 10):
        tree.delete(i)
    assert len(tree) == 0


def test_find() -> None:
    tree = Tree()
    assert tree.find(10) is None

    tree.insert(10)
    node = tree.find(10)
    assert node and node.value == 10

    for i in range(5):
        tree.insert(i)

    node = tree.find(4)
    assert node and node.value == 4

    tree.delete(10)
    assert tree.find(10) is None


def test_get_random_nodes() -> None:
    tree = Tree()
    # NOTE: See assets ch04_q11.svg
    for i in [3, 5, 7, 10, 15, 17, 20, 30]:
        tree.insert(i)

    rng = random.Random(14)
    counter = collections.Counter(
        tree.get_random_node(rng=rng).value for _ in range(128)
    )
    assert counter[3] == pytest.approx(16, abs=3)
