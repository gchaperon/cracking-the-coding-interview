import typing as tp

import linkedlist as ll


def intersection(
    left: ll.Node[str] | None, right: ll.Node[str] | None
) -> ll.Node[str] | None:
    def length(head: ll.Node[str] | None) -> int:
        return 0 if head is None else 1 + length(head.next)

    n, m = length(left), length(right)
    shortest, longest = (left, right) if n < m else (right, left)

    for _ in range(abs(n - m)):
        longest = tp.cast(ll.Node[str], longest).next

    while longest is not None and shortest is not None:
        if longest is shortest:
            return longest
        longest, shortest = longest.next, shortest.next
    return None


# ******************** Tests ********************
def test_intersection() -> None:
    l1 = ll.make_list("abcde")
    n = 2
    pointer = l1
    while pointer and n:
        pointer = pointer.next
        n -= 1
    l2 = ll.Node("f", pointer)

    assert intersection(l1, l2) is pointer


def test_intersection_simple() -> None:
    l1 = ll.make_list("abc")
    l2 = ll.make_list("abc")

    assert intersection(l1, l1) is l1
    assert intersection(l1, l2) is None
    assert intersection(l1, None) is None
    assert intersection(None, l1) is None
    assert intersection(None, None) is None
