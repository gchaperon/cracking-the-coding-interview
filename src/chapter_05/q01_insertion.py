def insert(n: int, m: int, i: int, j: int) -> int:
    spanlength = j - i + 1
    n_ones = (1 << spanlength) - 1
    mask = n_ones << i
    dock = n & ~mask
    return dock | (m << i)


# ******************** Tests ********************
def test_insert() -> None:
    n = 0b10000000000
    m = 0b10011
    assert insert(n, m, 2, 6) == 0b10001001100

    assert insert(0b11111, 0b100, 1, 3) == 0b11001
    assert insert(0b11111, 0b10, 1, 3) == 0b10101
