import typing as tp

import linkedlist as ll


def is_palindrome(head: ll.Node[str] | None) -> bool:
    n = 0
    stack = []
    pointer = head
    while pointer:
        n += 1
        stack.append(pointer.value)
        pointer = pointer.next

    pointer = head
    for _ in range(n // 2):
        if pointer and pointer.value != stack.pop():
            return False
        pointer = tp.cast(ll.Node[str], pointer).next
    return True


# ******************** Tests ********************
def test_is_palindrome() -> None:
    assert is_palindrome(ll.make_list(""))
    assert is_palindrome(ll.make_list("a"))
    assert is_palindrome(ll.make_list("abacaba"))
    assert is_palindrome(ll.make_list("abba"))

    assert not is_palindrome(ll.make_list("ab"))
    assert not is_palindrome(ll.make_list("abcd"))
