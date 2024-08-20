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
    i = 0
    # skip first one block
    while getbit(n, i) != 0:
        i += 1
    # find least significant non-trailing one
    while getbit(n, i) != 1:
        i += 1

    # count the ones before (inclusive)
    count = 0
    tmp = n
    for _ in range(i + 1):
        count += tmp & 1
        tmp >>= 1
    # set least significant trailing one to zero
    out = n
    out = updatebit(n, i, False)

    # free space before position i
    mask = ~((1 << i) - 1)
    out &= mask

    # set last bits to the largest number with `count` ones
    mask = (1 << count) - 1
    mask = mask << (i - count)
    return out | mask


def next_largest(n: int) -> int:
    i = 0
    # skip trailing zeros
    while getbit(n, i) == 0:
        i += 1

    # find least significant non trailing 0
    while getbit(n, i) != 0:
        i += 1

    # count the ones before position i
    count = 0
    tmp = n
    for _ in range(i):
        count += tmp & 1
        tmp >>= 1

    # set position i to  one
    out = updatebit(n, i, True)

    # clear all bits before position i
    mask = ~((1 << i) - 1)
    out &= mask

    # fill last bits with remaining ones
    mask = (1 << (count - 1)) - 1
    return out | mask


def next_numbers(n: int) -> tuple[int, int]:
    return next_smallest(n), next_largest(n)


# ******************** Tests ********************
def test_next_numbers() -> None:
    assert next_numbers(0b1000) == (0b100, 0b10000)
    assert next_numbers(0b1111011) == (0b1110111, 0b1111101)
    assert next_numbers(0b100100110000001) == (0b100100101100000, 0b100100110000010)
    assert next_numbers(0b11011001111100) == (0b11011001111010, 0b11011010001111)
