import linkedlist as ll


def detect_loop(head: ll.Node[str]) -> ll.Node[str]:
    slow = fast = head
    while True:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next  # type: ignore[assignment, union-attr]
        if slow is fast:
            break

    while head is not slow:
        head = head.next  # type: ignore[assignment]
        slow = slow.next  # type: ignore[assignment]

    return head


# ******************** Tests ********************
def _make_loop(head: ll.Node[str], value: str) -> None:
    last = head
    while last.next is not None:
        last = last.next

    beginning = head
    while beginning.next is not None and beginning.value != value:
        beginning = beginning.next

    last.next = beginning


def test_detect_loop() -> None:
    head = ll.make_list("abcde")
    assert head is not None
    _make_loop(head, "c")
    assert detect_loop(head).value == "c"

    head = ll.make_list("abcde")
    assert head is not None
    _make_loop(head, "a")
    assert detect_loop(head).value == "a"

    head = ll.make_list("abcde")
    assert head is not None
    _make_loop(head, "e")
    assert detect_loop(head).value == "e"

    head = ll.make_list("abcdefgh")
    assert head is not None
    _make_loop(head, "c")
    assert detect_loop(head).value == "c"
