def pairwise_swap(n: int) -> int:
    mask = 1
    while mask < n:
        mask = (mask << 2) + 1
    # NOTE: mask is like 0b1010...101
    jagged_shifted_left = (n & mask) << 1
    jagged_shifted_right = (n & (mask << 1)) >> 1
    return jagged_shifted_left | jagged_shifted_right


# ******************** Tests ********************
def test_pairwise_swap() -> None:
    assert pairwise_swap(0b0) == 0b0
    assert pairwise_swap(0b1) == 0b10
    assert pairwise_swap(0b11) == 0b11

    assert pairwise_swap(0b01_00_10_11_01) == 0b10_00_01_11_10
    assert pairwise_swap(0b10_10_01_11_01_01) == 0b01_01_10_11_10_10
