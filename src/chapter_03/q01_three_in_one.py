class Stacks:
    _array: list[int]
    _starts: list[int]
    _heads: list[int]

    def __init__(self, lengths: list[int]) -> None:
        self._array = [0] * sum(lengths)
        self._starts = [0]
        for length in lengths[:-1]:
            self._starts.append(self._starts[-1] + length)
        self._heads = [*self._starts]

    def __len__(self) -> int:
        return len(self._starts)

    def size(self, index: int) -> int:
        return self._heads[index] - self._starts[index]

    def empty(self, index: int) -> bool:
        return self.size(index) == 0

    def push(self, index: int, value: int) -> None:
        self._heads[index] += 1
        self._array[self._heads[index]] = value

    def peak(self, index: int) -> int:
        if self.empty(index):
            raise ValueError(f"Stack at {index=} is empty")

        return self._array[self._heads[index]]

    def pop(self, index: int) -> int:
        if self.empty(index):
            raise ValueError(f"Stack at {index=} is empty")

        value = self._array[self._heads[index]]
        self._heads[index] -= 1
        return value


# ******************** Tests ********************
def test_three_in_one() -> None:
    stacks = Stacks([100] * 3)
    assert len(stacks) == 3

    stacks.push(0, 3)
    stacks.push(0, 2)
    assert stacks.size(0) == 2
    assert stacks.pop(0) == 2
    assert stacks.peak(0) == 3
    assert stacks.pop(0) == 3
    assert stacks.empty(0)

    stacks.push(0, 1)
    stacks.push(1, 11)
    stacks.push(2, 21)
    stacks.push(2, 22)
    assert stacks.size(0) == 1
    assert stacks.size(1) == 1
    assert stacks.size(2) == 2
    assert stacks.peak(2) == 22
    stacks.pop(2)
    assert stacks.peak(2) == 21

    assert all(not stacks.empty(i) for i in range(3))

    for i in range(3):
        stacks.pop(i)

    assert all(stacks.empty(i) for i in range(3))
