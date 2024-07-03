import linkedlist as ll


def sum_list_reversed(
    left: ll.Node[int] | None, right: ll.Node[int] | None
) -> ll.Node[int] | None:
    def helper(
        left: ll.Node[int] | None, right: ll.Node[int] | None, carry: int
    ) -> ll.Node[int] | None:
        if left is None and right is None and carry == 0:
            return None
        else:
            carry, value = divmod(
                (0 if left is None else left.value)
                + (0 if right is None else right.value)
                + carry,
                10,
            )
            return ll.Node(
                value, helper(left and left.next, right and right.next, carry)
            )

    return helper(left, right, 0)


def sum_list_forward(
    left: ll.Node[int] | None, right: ll.Node[int] | None
) -> ll.Node[int] | None:
    def helper(
        left: ll.Node[int] | None, right: ll.Node[int] | None
    ) -> tuple[int, ll.Node[int] | None]:
        if left is None and right is None:
            return 0, None
        else:
            carry, tail = helper(left and left.next, right and right.next)
            carry, value = divmod(
                (0 if left is None else left.value)
                + (0 if right is None else right.value)
                + carry,
                10,
            )
            return carry, ll.Node(value, tail)

    carry, tail = helper(left, right)
    return ll.Node(carry, tail) if carry else tail


# ******************** Tests ********************


def test_sum_list_reversed() -> None:
    assert sum_list_reversed(
        ll.make_list([7, 1, 6]), ll.make_list([5, 9, 2])
    ) == ll.make_list([2, 1, 9])


def test_sum_list_forward() -> None:
    assert sum_list_forward(
        ll.make_list([6, 1, 7]), ll.make_list([2, 9, 5])
    ) == ll.make_list([9, 1, 2])
