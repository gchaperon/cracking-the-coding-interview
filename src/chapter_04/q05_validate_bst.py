import itertools
import typing as tp

from graphs import Node


def is_bst(root: Node[int] | None) -> bool:
    def traverse(root: Node[int] | None) -> tp.Iterable[int]:
        if root is not None:
            yield from itertools.chain(
                traverse(root.left),
                [root.value],
                traverse(root.right),
            )

    def is_sorted(it: tp.Iterable[int]) -> bool:
        return all(a <= b for a, b in itertools.pairwise(it))

    return is_sorted(traverse(root))


# ******************** Tests ********************
def test_is_bst() -> None:
    assert is_bst(None)
    assert is_bst(Node(1))
    assert is_bst(Node(2, Node(1)))
    assert not is_bst(Node(2, None, Node(1)))

    # See file assets/c04_q04_balanced.svg. Same structure with different
    # values.
    assert is_bst(
        Node(
            10,
            Node(
                5,
                Node(3, Node(0)),
                Node(7, Node(6), Node(8)),
            ),
            Node(20, None, Node(100)),
        )
    )
    assert not is_bst(
        Node(
            1,
            Node(
                2,
                Node(3, Node(4)),
                Node(7, Node(11), Node(5)),
            ),
            Node(20, None, Node(6)),
        )
    )
