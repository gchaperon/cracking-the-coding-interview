class SetOfStacks:
    max_height: int

    _stacks: list[list[int]]

    def __init__(self, max_height: int) -> None:
        self.max_height = max_height
        self._stacks = []

    def push(self, value: int) -> None:
        if self.size() == 0 or len(self._stacks[-1]) == self.max_height:
            self._stacks.append([value])
        else:
            self._stacks[-1].append(value)

    def pop(self) -> int:
        if self.empty():
            raise IndexError
        value = self._stacks[-1].pop()
        if not self._stacks[-1]:
            self._stacks.pop()
        return value

    def size(self) -> int:
        return sum(self.sizes())

    def sizes(self) -> list[int]:
        return [len(stack) for stack in self._stacks]

    def empty(self) -> bool:
        return self.size() == 0

    def pop_at(self, index: int) -> int:
        if not 0 <= index < len(self._stacks) or self.empty():
            raise IndexError

        value = self._stacks[index].pop()
        if not self._stacks[index]:
            del self._stacks[index]
        return value


# ******************** Tests ********************
def test_set_of_stacks() -> None:
    max_size = 3
    stack = SetOfStacks(max_size)
    for i in range(7):
        stack.push(i)

    assert stack.size() == 7
    assert all(s <= 3 for s in stack.sizes())

    assert stack.pop() == 6
    for _ in range(5):
        stack.pop()
    assert stack.pop() == 0
    assert stack.empty()


def test_pop_at() -> None:
    max_size = 3
    stack = SetOfStacks(max_size)
    for i in range(7):
        stack.push(i)

    assert stack.size() == 7
    assert stack.pop_at(1) == 5
    assert stack.size() == 6

    for _ in range(max_size - 1):
        stack.pop_at(1)
    assert stack.size() == 4
    assert len(stack.sizes()) == 2

    for _ in range(stack.size()):
        stack.pop()

    assert stack.empty()
    assert len(stack.sizes()) == 0
