def insert(n: int, m: int, i: int, j: int) -> int:
    mask = (j - i + 1) << i
    dock = n & ~mask
    return dock | (m << i)


# ******************** Tests ********************
def test_insert() -> None:
    n = 0b10000000000
    m = 0b10011
    assert insert(n, m, 2, 6) == 0b10001001100
