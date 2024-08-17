import itertools
import typing as tp

from graphs import Node


def is_child(value: str, tree: Node[str] | None) -> bool:
    if tree is None:
        return False
    elif value == tree.value:
        return True
    else:
        return is_child(value, tree.left) or is_child(value, tree.right)


def first_common_ancestor(tree: Node[str], a: str, b: str) -> str | None:
    def traverse(node: Node[str] | None) -> tp.Iterable[Node[str]]:
        if node is not None:
            yield from itertools.chain(
                traverse(node.left),
                traverse(node.right),
                [node],
            )

    for node in traverse(tree):
        if is_child(a, node) and is_child(b, node):
            return node.value
    return None


# ******************** Tests ********************
def test_is_chiled() -> None:
    assert not is_child("a", None)
    assert is_child("a", Node("a"))
    assert not is_child("b", Node("a"))
    assert is_child("b", Node("a", Node("b")))

    assert is_child("k", Node("g", Node("h"), Node("i", None, Node("j", Node("k")))))


def test_first_common_ancestor() -> None:
    assert first_common_ancestor(Node("a"), "a", "a") == "a"
    assert first_common_ancestor(Node("a", Node("b")), "a", "b") == "a"
    assert first_common_ancestor(Node("a", None, Node("b")), "a", "b") == "a"

    # NOTE: see assets/ch04_q08.svg
    tree = Node(
        "a",
        Node(
            "b",
            Node("c"),
            Node(
                "d",
                Node("e"),
                Node("f"),
            ),
        ),
        Node(
            "g",
            Node("h"),
            Node(
                "i",
                None,
                Node(
                    "j",
                    Node("k"),
                ),
            ),
        ),
    )
    assert first_common_ancestor(tree, "e", "g") == "a"
    assert first_common_ancestor(tree, "e", "k") == "a"
    assert first_common_ancestor(tree, "e", "f") == "d"
    assert first_common_ancestor(tree, "c", "e") == "b"
    assert first_common_ancestor(tree, "k", "j") == "j"
    assert first_common_ancestor(tree, "k", "h") == "g"
    assert first_common_ancestor(tree, "h", "g") == "g"
    assert first_common_ancestor(tree, "k", "i") == "i"
