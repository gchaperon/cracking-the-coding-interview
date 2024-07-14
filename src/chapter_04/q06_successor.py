from __future__ import annotations

import dataclasses
import itertools
import typing as tp

from graphs import Node


@dataclasses.dataclass
class NodeWithParent:
    value: int
    left: NodeWithParent | None = None
    right: NodeWithParent | None = None
    parent: NodeWithParent | None = None


def addparent(
    node: Node[int] | None, parent: NodeWithParent | None = None
) -> NodeWithParent | None:
    if node is None:
        return None
    else:
        current = NodeWithParent(node.value, None, None, parent)
        current.left = addparent(node.left, current)
        current.right = addparent(node.right, current)
        return current


def successor_no_parent(root: Node[int], target: Node[int]) -> int:
    def traverse(node: Node[int] | None) -> tp.Iterable[Node[int]]:
        if node is not None:
            yield from itertools.chain(
                traverse(node.left),
                [node],
                traverse(node.right),
            )

    def is_not_target(node: Node[int]) -> bool:
        return node is not target

    return next(
        itertools.islice(
            itertools.dropwhile(is_not_target, traverse(root)),
            1,
            None,
        )
    ).value


def successor_with_parent(target: NodeWithParent) -> int:
    def findmin(tree: NodeWithParent) -> int:
        if tree.left is None:
            return tree.value
        else:
            return findmin(tree.left)

    def first_parent_to_the_right(node: NodeWithParent) -> NodeWithParent:
        assert node.parent
        if node.parent.left is node:
            return node.parent
        else:
            return first_parent_to_the_right(node.parent)

    if target.right is not None:
        return findmin(target.right)
    else:
        return first_parent_to_the_right(target).value


# ******************** Tests ********************
def test_successor_no_parent() -> None:
    # See file assets/c04_q04_balanced.svg. Same structure with different
    # values.
    tree = Node(
        10,
        Node(
            5,
            Node(3, Node(0)),
            Node(7, Node(6), Node(8)),
        ),
        Node(20, None, Node(100)),
    )
    # NOTE: assertions for tree children (before each and) exist solely for
    # type checking purposes
    assert successor_no_parent(tree, tree) == 20
    assert tree.left and successor_no_parent(tree, tree.left) == 6
    assert tree.right and successor_no_parent(tree, tree.right) == 100
    assert tree.left.left and successor_no_parent(tree, tree.left.left) == 5
    assert (
        tree.left.right
        and tree.left.right.right
        and successor_no_parent(tree, tree.left.right.right) == 10
    )


def test_successor_with_parent() -> None:
    # See file assets/c04_q04_balanced.svg. Same structure with different
    # values.
    noparent = Node(
        10,
        Node(
            5,
            Node(3, Node(0)),
            Node(7, Node(6), Node(8)),
        ),
        Node(20, None, Node(100)),
    )
    tree = addparent(noparent)
    # NOTE: assertions for tree children (before each and) exist solely for
    # type checking purposes
    assert tree and successor_with_parent(tree) == 20
    assert tree.left and successor_with_parent(tree.left) == 6
    assert tree.right and successor_with_parent(tree.right) == 100
    assert tree.left.left and successor_with_parent(tree.left.left) == 5
    assert tree.left.right
    assert tree.left.right.right
    assert successor_with_parent(tree.left.right.right) == 10
