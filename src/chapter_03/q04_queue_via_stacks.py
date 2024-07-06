def _pour(from_: list[int], to: list[int]) -> None:
    while from_:
        to.append(from_.pop())


class MyQueue:
    _left: list[int]
    _right: list[int]

    def __init__(self) -> None:
        self._left = []
        self._right = []

    def remove(self) -> int:
        _pour(self._left, self._right)
        return self._right.pop()

    def add(self, value: int) -> None:
        _pour(self._right, self._left)
        self._left.append(value)

    def size(self) -> int:
        return len(self._left) + len(self._right)

    def empty(self) -> bool:
        return self.size() == 0


# ******************** Tests ********************
def test_my_queue() -> None:
    queue = MyQueue()

    assert queue.empty()

    queue.add(2)
    assert queue.size() == 1
    assert queue.remove() == 2
    assert queue.empty()

    for i in range(10):
        queue.add(i)

    assert queue.remove() == 0
    queue.add(100)
    assert queue.size() == 10

    for _ in range(9):
        queue.remove()

    assert queue.remove() == 100

    assert queue.empty()
