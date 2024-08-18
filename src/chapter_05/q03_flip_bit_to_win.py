import typing as tp


def flip_bit_to_win(value: int) -> int:
    def potentialiter(value: int) -> tp.Iterable[int]:
        zero_count = 0
        last_window = 0
        current_window = 0
        while value > 0:
            first_digit = value & 1
            if first_digit:
                current_window += 1
            else:
                if zero_count > 0:
                    yield current_window + last_window
                last_window = current_window
                current_window = 0
                zero_count += 1
            value >>= 1
        yield current_window

    def bitlen(value: int) -> int:
        if value == 0:
            return 1

        count = 0
        while value > 0:
            value >>= 1
            count += 1
        return count

    maxsum = max(potentialiter(value))
    if maxsum == bitlen(value):
        return bitlen(value)
    return maxsum + 1


# ******************** Tests ********************
def test_flip_bin_to_win() -> None:
    assert flip_bit_to_win(0b11011101111) == 8

    assert flip_bit_to_win(0b111) == 3
    assert flip_bit_to_win(0b0) == 1
    assert flip_bit_to_win(0b111000000) == 4
    assert flip_bit_to_win(0b10001100) == 3
    assert flip_bit_to_win(0b10011) == 3
