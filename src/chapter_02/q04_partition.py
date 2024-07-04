import linkedlist as ll


def is_partitioned(head: ll.Node[int] | None, value: int) -> bool:
    switched = False
    while head is not None:
        if switched and head.value < value:
            return False
        if not switched and head.value >= value:
            switched = True
        head = head.next

    return True


def partition(head: ll.Node[int] | None, value: int) -> ll.Node[int] | None:
    low = ll.Anchor[int]()
    last_low: ll.HasNext[int] = low
    high = ll.Anchor[int]()
    last_high: ll.HasNext[int] = high
    while head is not None:
        # deattach current node
        tmp = head
        head = head.next
        tmp.next = None
        # attach to correct list
        if tmp.value < value:
            last_low.next = tmp
            last_low = last_low.next
        else:
            last_high.next = tmp
            last_high = last_high.next
    last_low.next = high.next
    return low.next


# ******************** Tests ********************


def test_is_partitioned() -> None:
    assert not is_partitioned(ll.make_list([3, 5, 8, 5, 10, 2, 1]), value=5)
    assert is_partitioned(ll.make_list([3, 1, 2, 10, 5, 5, 8]), value=5)


def test_partition() -> None:
    assert is_partitioned(
        partition(ll.make_list([3, 5, 8, 5, 10, 2, 1]), value=5), value=5
    )
