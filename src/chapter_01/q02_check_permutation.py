import collections


def is_permutation(left: str, right: str) -> bool:
    """Check if left and right strings are permutations of each other.

    A string is a permutation of another if they both have the same individual
    characters, and the same count of each character.
    """
    return collections.Counter(left) == collections.Counter(right)


# ******************** Tests ********************
def test_is_permutation() -> None:
    assert is_permutation("", "")
    assert is_permutation(
        "a string is a permutation of itself", "a string is a permutation of itself"
    )
    assert is_permutation("aab", "aba")
    assert is_permutation("aa", "aa")
    assert is_permutation("abaasdfqwe", "aaabdefqsw")
    assert not is_permutation("", "a")
    assert not is_permutation("ab", "aab")
    assert not is_permutation("abc", "abd")
