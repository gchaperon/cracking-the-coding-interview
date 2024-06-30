import linkedlist as ll


def remove_dups(head: ll.Node[int]) -> ll.Node[int]:
    """Removes the duplicates in a linked list.

    Has O(n) time and space complexity.

    FOLLOW UP (answer): We could do this in O(n**2) time and O(1) space
    complexity by iterating over the entire array for each value, checking if
    it's already present in the array and removing it accordingly.
    """
    seen: set[int] = set()

    def remove_next(node: ll.Node[int]) -> None:
        if node is None or node.next is None:
            return
        node.next = node.next.next

    current = head
    prev = None
    while current is not None:
        if current.value in seen:
            remove_next(prev)
            current = current.next
        else:
            seen.add(current.value)
            prev = current
            current = current.next
    return head


# ******************** Tests ********************
def test_remove_dups() -> None:
    assert remove_dups(ll.make_list([])) == ll.make_list([])
    assert remove_dups(ll.make_list([1, 1])) == ll.make_list([1])
    assert remove_dups(ll.make_list(range(5))) == ll.make_list(range(5))

    assert remove_dups(ll.make_list([1, 2, 3, 1])) == ll.make_list([1, 2, 3])
    assert remove_dups(ll.make_list([3, 5, 1, 1, 5, 5, 2, 3, 3, 3])) == ll.make_list(
        [3, 5, 1, 2]
    )
