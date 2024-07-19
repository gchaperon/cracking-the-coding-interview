import collections

from graphs import Node


def paths_with_sum(node: Node[int] | None, target: int) -> int:
    def impl(
        node: Node[int] | None, target: int, cumsum: int, counter: dict[int, int]
    ) -> int:
        if node is None:
            return 0
        else:
            cumsum = cumsum + node.value
            counter[cumsum] += 1
            leftcount = impl(node.left, target, cumsum, counter)
            rightcount = impl(node.right, target, cumsum, counter)
            counter[cumsum] -= 1

            return (
                (cumsum == target) + counter[cumsum - target] + leftcount + rightcount
            )

    return impl(node, target, 0, counter=collections.defaultdict(int))


# ******************** Tests ********************
def test_paths_with_sum() -> None:
    assert paths_with_sum(None, 0) == 0
    assert paths_with_sum(None, -3) == 0
    assert paths_with_sum(None, 10) == 0

    assert paths_with_sum(Node(0), 0) == 1
    assert paths_with_sum(Node(10), 0) == 0
    assert paths_with_sum(Node(10), 10) == 1

    assert paths_with_sum(Node(1, Node(-3)), -2) == 1

    assert paths_with_sum(Node(1, Node(-1, Node(1, Node(-1)))), 0) == 4

    tree = Node(
        10,
        Node(
            5,
            Node(
                3,
                Node(3),
                Node(-2),
            ),
            Node(
                2,
                None,
                Node(1),
            ),
        ),
        Node(
            -3,
            None,
            Node(11),
        ),
    )
    assert paths_with_sum(tree, 8) == 3
