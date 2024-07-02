import typing as tp

import linkedlist as ll


def kth_to_last(head: ll.Node[str] | None, k: int) -> str:
    if head is None:
        raise ValueError("Empty list")

    right: ll.Node[str] | None = head
    for _ in range(k):
        if right is None:
            raise ValueError(f"Not enough values in list for {k=}")
        right = right.next
    left = head
    while right is not None:
        right = right.next
        left = tp.cast(ll.Node[str], left.next)
    return left.value


# ******************** Tests ********************
def test_kth_to_last() -> None:
    assert kth_to_last(ll.make_list("abcde"), 1) == "e"
    assert kth_to_last(ll.make_list("abcde"), 3) == "c"
    assert kth_to_last(ll.make_list("abcde"), 5) == "a"
    assert kth_to_last(ll.make_list("a"), 1) == "a"


def test_kth_to_last_raises() -> None:
    import pytest

    with pytest.raises(ValueError):
        kth_to_last(ll.make_list(""), 1)
    with pytest.raises(ValueError):
        kth_to_last(ll.make_list("abc"), 4)
