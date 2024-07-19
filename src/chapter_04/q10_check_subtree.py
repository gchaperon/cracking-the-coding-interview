from graphs import Node


def subtree_same_root(tree: Node[str] | None, subtree: Node[str] | None) -> bool:
    if subtree is None:
        return True
    elif tree is None:
        return False
    else:
        return (
            tree.value == subtree.value
            and subtree_same_root(tree.left, subtree.left)
            and subtree_same_root(tree.right, subtree.right)
        )


def check_subtree(tree: Node[str] | None, subtree: Node[str] | None) -> bool:
    if subtree is None:
        return True
    elif tree is None:
        return False
    else:
        if tree.value == subtree.value:
            return subtree_same_root(tree.left, subtree.left) and subtree_same_root(
                tree.right, subtree.right
            )
        else:
            return check_subtree(tree.left, subtree) or check_subtree(
                tree.right, subtree
            )


# ******************** Tests ********************
def test_check_subtree() -> None:
    assert check_subtree(None, None)
    assert check_subtree(Node("a"), Node("a"))
    assert check_subtree(Node("a"), None)
    assert check_subtree(Node("a", Node("b")), Node("b"))
    assert not check_subtree(Node("a"), Node("b"))
    assert not check_subtree(None, Node("a"))

    # NOTE: see assets/ch04_q10.svg
    T1 = Node(
        "a",
        Node(
            "b",
            Node("c"),
            Node(
                "d",
                None,
                Node(
                    "e",
                    Node("f"),
                    Node(
                        "g",
                        None,
                        Node("h"),
                    ),
                ),
            ),
        ),
        Node(
            "i",
            Node(
                "j",
                Node("k"),
                Node(
                    "l",
                    Node("m"),
                ),
            ),
        ),
    )
    # T2.1
    assert check_subtree(
        T1,
        Node(
            "i",
            Node(
                "j",
                Node("k"),
                Node("l"),
            ),
        ),
    )
    # T2.2
    assert check_subtree(
        T1,
        Node(
            "a",
            Node("b"),
            Node("i"),
        ),
    )
    # T2.3
    assert check_subtree(
        T1,
        Node(
            "e",
            None,
            Node(
                "g",
                None,
                Node("h"),
            ),
        ),
    )
    # T2.4
    assert check_subtree(
        T1,
        Node(
            "b",
            Node("c"),
        ),
    )
    # T2.5
    assert not check_subtree(
        T1,
        Node(
            "i",
            Node("j"),
            Node("k"),
        ),
    )
    # T2.6
    assert not check_subtree(
        T1,
        Node(
            "a",
            Node("b"),
            Node("t"),
        ),
    )
    # Extra, counterexample to first naive impl
    assert not check_subtree(
        T1,
        Node(
            "b",
            None,
            Node("f"),
        ),
    )
