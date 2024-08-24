def is_power_of_two(n: int) -> bool:
    return (n & (n - 1)) == 0


# ******************** Tests ********************
def test_is_power_of_two() -> None:
    assert is_power_of_two(1)
    assert is_power_of_two(2)
    assert is_power_of_two(4)
    assert is_power_of_two(8)
    assert is_power_of_two(16)
    assert is_power_of_two(1024)

    assert not is_power_of_two(3)
    assert not is_power_of_two(123)
    assert not is_power_of_two(543)
    assert not is_power_of_two(6)
