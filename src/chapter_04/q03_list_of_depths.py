import collections
import itertools
import typing as tp

from graphs import Node


def list_of_depths(tree: Node[int] | None) -> list[list[int]]:
    def traverse(
        node: Node[int] | None, depth: int
    ) -> tp.Iterable[tuple[Node[int], int]]:
        if node is not None:
            yield from itertools.chain(
                [(node, depth)],
                traverse(node.left, depth + 1),
                traverse(node.right, depth + 1),
            )

    depths = collections.defaultdict(list)
    for node, depth in traverse(tree, 0):
        depths[depth].append(node.value)
    return list(depths.values())


# ******************** Tests ********************
def test_list_of_depths() -> None:
    assert list_of_depths(None) == []
    assert list_of_depths(Node(1)) == [[1]]
    assert list_of_depths(Node(1, None, Node(2))) == [[1], [2]]
    assert list_of_depths(Node(1, Node(2), Node(3))) == [[1], [2, 3]]

    tree = Node(
        1,
        Node(
            2,
            Node(3),
            Node(
                4,
                None,
                Node(5),
            ),
        ),
        Node(
            6,
            Node(
                7,
                Node(
                    8,
                    None,
                    Node(9),
                ),
            ),
            Node(
                10,
                Node(11),
                Node(
                    12,
                    None,
                    Node(
                        13,
                        Node(14),
                    ),
                ),
            ),
        ),
    )
    assert list_of_depths(tree) == [
        [1],
        [2, 6],
        [3, 4, 7, 10],
        [5, 8, 11, 12],
        [9, 13],
        [14],
    ]
