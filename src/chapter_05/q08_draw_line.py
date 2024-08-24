def drawrange(start: int = 0, finish: int = 7) -> int:
    rangesize = finish - start + 1
    return ((1 << rangesize) - 1) << (7 - finish)


def drawline(screen: bytes, width: int, x1: int, x2: int, y: int) -> bytes:
    assert width % 8 == 0
    height = len(screen) * 8 // width

    byte1, bit1 = divmod(x1, 8)
    byte2, bit2 = divmod(x2, 8)
    out = bytearray(screen)

    bytestart = width // 8 * (height - y - 1)
    if byte1 == byte2:
        out[bytestart + byte1] = drawrange(bit1, bit2)
    else:
        out[bytestart + byte1] = drawrange(bit1, 7)
        out[bytestart + byte2] = drawrange(0, bit2)
        for byte in range(byte1 + 1, byte2):
            out[bytestart + byte] = drawrange(0, 7)
    return bytes(out)


def printscreen(screen: bytes, width: int) -> None:
    import itertools

    for row in itertools.batched(screen, width // 8):
        print(" ".join(f"{value:08b}" for value in row))


# ******************** Tests ********************
def test_drawline_multiple_bytes() -> None:
    x1, x2 = 5, 17
    y = 3
    width = 24
    # fmt: off
    # NOTE: width=24, height=8
    screen = bytes(
        [
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
        ]
    )
    target = bytes(
        [
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000111, 0b11111111, 0b11000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
        ]
    )
    # fmt: on

    result = drawline(screen, width, x1, x2, y)
    assert result == target


def test_drawline_single_byte() -> None:
    x1, x2 = 1, 5
    y = 7
    width = 24
    # fmt: off
    # NOTE: width=24, height=8
    screen = bytes(
        [
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
        ]
    )
    target = bytes(
        [
            0b01111100, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
            0b00000000, 0b00000000, 0b00000000,
        ]
    )
    # fmt: on

    result = drawline(screen, width, x1, x2, y)
    assert result == target
