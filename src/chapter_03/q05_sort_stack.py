import itertools


def _insert_sorted(value: int, stack: list[int], buffer: list[int]) -> None:
    for n in itertools.count():
        if not stack or stack[-1] >= value:
            break
        buffer.append(stack.pop())

    stack.append(value)
    for _ in range(n):
        stack.append(buffer.pop())


def stacksort(stack: list[int]) -> None:
    buffer: list[int] = []

    while stack:
        _insert_sorted(stack.pop(), buffer, stack)

    while buffer:
        stack.append(buffer.pop())


# ******************** Tests ********************
def test_insert_sorted() -> None:
    stack = [10, 5, 4, 1]
    _insert_sorted(4, stack, [])
    assert len(stack) == 5
    assert sorted(stack, reverse=True) == stack


def test_sort() -> None:
    import random

    stack: list[int] = []
    stacksort(stack)
    assert stack == []

    stack = list(range(100))
    for _ in range(5):
        random.shuffle(stack)
        stacksort(stack)
        assert stack == sorted(stack)
