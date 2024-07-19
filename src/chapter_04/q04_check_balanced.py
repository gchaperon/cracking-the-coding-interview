from graphs import Node


def is_balanced(root: Node[str] | None) -> bool:
    def helper(node: Node[str] | None) -> tuple[bool, int]:
        if node is None:
            return True, 0
        else:
            lbalance, lheight = helper(node.left)
            rbalance, rheight = helper(node.right)

            children_balanced = lbalance and rbalance
            height_difference = abs(lheight - rheight)

            tree_height = 1 + max(lheight, rheight)
            return children_balanced and height_difference <= 1, tree_height

    result, _ = helper(root)
    return result


# ******************** Tests ********************
def test_is_balanced() -> None:
    assert is_balanced(None)
    assert is_balanced(Node("a"))
    assert is_balanced(Node("a", Node("b")))
    assert not is_balanced(Node("a", None, Node("b", Node("c"))))

    # See file assets/c04_q04_balanced.svg
    assert is_balanced(
        Node(
            "a",
            Node(
                "b",
                Node("c", Node("d")),
                Node("e", Node("f"), Node("g")),
            ),
            Node("h", None, Node("i")),
        )
    )
    # See file assets/c04_q04_inbalanced.svg
    assert not is_balanced(
        Node(
            "a",
            Node(
                "b",
                None,
                Node("e", Node("f"), Node("g")),
            ),
            Node("h", None, Node("i")),
        )
    )
