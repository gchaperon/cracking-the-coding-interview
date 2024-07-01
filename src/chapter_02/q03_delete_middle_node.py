import linkedlist as ll


def delete_middle(node: ll.Node[str]) -> None:
    if node.next is None:
        raise ValueError("Node cannot be the last node")

    node.value = node.next.value
    node.next = node.next.next


# ******************** Tests ********************
def test_delete_middle() -> None:
    llist = ll.make_list("abcdef")
    node = llist.next.next  # type: ignore[union-attr]
    assert node is not None
    assert node.value == "c"

    delete_middle(node)
    assert llist == ll.make_list("abdef")
