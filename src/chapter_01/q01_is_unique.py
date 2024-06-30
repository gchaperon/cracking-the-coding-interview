import typing as tp
import string
import itertools

def is_unique(value: str) -> bool:
    """Checks if all characters in string are unique.

    Assumes ascii characters.
    """
    assert all(c in string.ascii_letters for c in value), "All charactess must belong to the ASCII range."
    hashmap = {}
    for c in value:
        if c in hashmap:
            return False
        hashmap[c] = 1
    return True

def is_unique_no_struct(value: str) -> bool:
    for prev, current in itertools.pairwise(sorted(value)):
        if prev == current:
            return False
    return True


# ******************** Tests ********************

def _test_unique_fun(fun: tp.Callable[[str], bool]) -> None:
    assert fun("")
    assert fun("abcd")
    assert not fun("aa")
    assert not fun("aba")
    assert not fun("afjowlpa")
    assert fun("A")

def test_is_unique() -> None:
    _test_unique_fun(is_unique)

def test_is_unique_no_struct() -> None:
    _test_unique_fun(is_unique_no_struct)
