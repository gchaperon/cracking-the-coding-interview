def nbitflips(n: int, m: int) -> int:
    count = 0
    xor = n ^ m
    while xor:
        count += xor & 1
        xor >>= 1

    return count


# ******************** Tests ********************
def test_nbitflips() -> None:
    assert nbitflips(0b11101, 0b01111) == 2

    assert nbitflips(0b0, 0b0) == 0
    assert nbitflips(0b1, 0b1) == 0

    assert nbitflips(0b0, 0b1) == 1
    assert nbitflips(0b111111, 0b0) == 6
