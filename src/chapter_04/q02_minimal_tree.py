import itertools
import typing as tp

import graphs


def height(tree: graphs.Node[int] | None) -> int:
    return 0 if tree is None else 1 + max(height(tree.left), height(tree.right))


def traverse_inorder(tree: graphs.Node[int] | None) -> list[int]:
    def traverse(tree: graphs.Node[int] | None) -> tp.Iterable[int]:
        if tree is not None:
            yield from itertools.chain(
                traverse(tree.left), [tree.value], traverse(tree.right)
            )

    return list(traverse(tree))


def minimal_tree(array: list[int]) -> graphs.Node[int] | None:
    n = len(array)
    if n == 0:
        return None
    else:
        half = n // 2
        return graphs.Node(
            array[half],
            minimal_tree(array[:half]),
            minimal_tree(array[half + 1 :]),
        )


# ******************** Tests ********************
def test_height() -> None:
    assert height(None) == 0
    assert height(graphs.Node(3)) == 1
    assert height(graphs.Node(1, graphs.Node(2))) == 2
    assert (
        height(
            graphs.Node(
                1,
                None,
                graphs.Node(
                    3,
                    None,
                    graphs.Node(4, None, graphs.Node(5)),
                ),
            )
        )
        == 4
    )


def test_traverse_in_order() -> None:
    assert traverse_inorder(None) == []
    assert traverse_inorder(graphs.Node(1)) == [1]
    assert traverse_inorder(graphs.Node(1, graphs.Node(2))) == [2, 1]
    assert traverse_inorder(graphs.Node(1, None, graphs.Node(2))) == [1, 2]
    assert traverse_inorder(
        graphs.Node(
            1,
            graphs.Node(
                2,
                graphs.Node(3, graphs.Node(4), graphs.Node(5)),
                graphs.Node(6, graphs.Node(7), graphs.Node(8)),
            ),
            graphs.Node(9, graphs.Node(10)),
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
