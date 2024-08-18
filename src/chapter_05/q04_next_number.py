def bitlen(n: int) -> int:
    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n >>= 1
    return count


def getbit(n: int, i: int) -> int:
    mask = 1 << i
    return int(n & mask != 0)


def updatebit(n: int, i: int, value: bool) -> int:
    mask = ~(1 << i)
    return (n & mask) | (value << i)


def next_smallest(n: int) -> int:
    most_significant_zero = bitlen(n) - 1
    while getbit(n, most_significant_zero) != 0:
        most_significant_zero -= 1

    temp = updatebit(n, most_significant_zero, True)
    return updatebit(temp, most_significant_zero + 1, False)


def next_largest(n: int) -> int:
    first_one = 0
    while getbit(n, first_one) != 1:
        first_one += 1
    # i should be callend something like least_significant_zero_after_first_one
    # (or similar), but it's too long to write everywhere
    i = first_one
    while getbit(n, i) != 0:
        i += 1
    temp = updatebit(n, i, True)
    return updatebit(temp, i - 1, False)


def next_numbers(n: int) -> tuple[int, int]:
    return next_smallest(n), next_largest(n)


# ******************** Tests ********************
def test_next_numbers() -> None:
    assert next_numbers(0b1001) == (0b101, 0b1010)
    assert next_numbers(0b11001) == (0b10101, 0b11010)
    assert next_numbers(0b100111) == (0b10111, 0b101011)
    assert next_numbers(0b1100110011) == (0b1010110011, 0b1100110101)

    assert next_numbers(0b10) == (0b1, 0b100)
    assert next_numbers(0b10000) == (0b1000, 0b100000)
    assert next_numbers(0b110110) == (0b101110, 0b111010)
