class StackMin:
    _stack: list[int]
    _mins: list[int]

    def __init__(self) -> None:
        self._stack = []
        self._mins = []

    def empty(self) -> bool:
        return len(self._stack) == 0

    def push(self, value: int) -> None:
        if self.empty() or value <= self._mins[-1]:
            self._mins.append(value)
        self._stack.append(value)

    def min(self) -> int:
        if self.empty():
            raise ValueError
        return self._mins[-1]

    def pop(self) -> int:
        if self.empty():
            raise ValueError
        value = self._stack.pop()
        if value == self._mins[-1]:
            self._mins.pop()

        return value


# ******************** Tests ********************
def test_stack_min() -> None:
    stack = StackMin()

    assert stack.empty()

    stack.push(3)
    assert stack.min() == 3

    stack.push(1)
    assert stack.min() == 1
    stack.push(1)
    assert stack.min() == 1

    stack.pop()
    assert stack.min() == 1
    stack.pop()
    assert stack.min() == 3
