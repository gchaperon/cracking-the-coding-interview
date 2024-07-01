import itertools
import typing as tp


def compress(string: str) -> str:
    if not string:
        return ""

    parts = []
    key = string[0]
    count = 1
    for c in string[1:]:
        if c == key:
            count += 1
        else:
            parts.append((key, count))
            key = c
            count = 1
    parts.append((key, count))

    compressed = "".join(f"{key}{count}" for key, count in parts)
    return compressed if len(compressed) < len(string) else string


def compress_to_easy(string: str) -> str:
    compressed = "".join(
        f"{key}{len(list(group))}" for key, group in itertools.groupby(string)
    )
    return compressed if len(compressed) < len(string) else string


# ******************** Tests ********************
def _test_compress_fn(function: tp.Callable[[str], str]) -> None:
    assert function("") == ""
    assert function("abcd") == "abcd"
    assert function("aaabcd") == "aaabcd"
    assert function("aaaaabcd") == "aaaaabcd"
    assert function("aaaaaabcd") == "a6b1c1d1"
    assert function("aabcccccaaa") == "a2b1c5a3"


def test_compress() -> None:
    _test_compress_fn(compress)


def test_compress_to_easy() -> None:
    _test_compress_fn(compress_to_easy)
