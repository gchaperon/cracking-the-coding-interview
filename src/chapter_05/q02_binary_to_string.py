import itertools
import typing as tp


def integer_ratio(f: float) -> tuple[int, int]:
    n = 0
    while f - int(f) != 0:
        f *= 10
        n += 1
    return int(f), 10**n


def bin2str(x: float) -> str:
    it = iter(bin_decimal_division(*integer_ratio(x)))
    out = "0." + "".join(itertools.islice(it, 32))
    try:
        next(it)
        return "ERROR"
    except StopIteration:
        return out


def bin_decimal_division(n: int, m: int) -> tp.Iterable[str]:
    assert n < m
    remainder = n
    while remainder != 0:
        remainder <<= 1
        if remainder < m:
            yield "0"
        else:
            yield "1"
            remainder %= m


# ******************** Tests ********************


def test_bin2str() -> None:
    assert bin2str(0.5) == "0.1"
    assert bin2str(0.25) == "0.01"
    assert bin2str(0.875) == "0.111"

    assert bin2str(0.72) == "ERROR"
    assert bin2str(0.2) == "ERROR"
