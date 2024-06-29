def one_away(left: str, right: str) -> bool:
    """Checks if left and right are one (or zero) edit away.

    Edits can be character insertion, deletion or replacement.

    The two strings are (at most) one edit away if, after finding the first
    diverging character, we attempt to perform one of the three types of edits
    and the remainding strings are equal.
    """
    short, long = sorted([left, right], key=len)
    for i in range(len(long)):
        if i >= len(short) or (short[i] != long[i]):
            # check if by inserting, removing or replacing a character the
            # remainding strings are equal
            insert = short[i:] == long[i + 1:]
            remove = short[i+1:] == long[i:]
            replace = short[i+1:] == long[i+1:]
            return insert or remove or replace
    return True

# ******************** Tests ******************** 

def test_one_away() -> None:
    assert one_away("pale", "ple")
    assert one_away("pales", "pale")
    assert one_away("pale", "bale")
    assert not one_away("pale", "bake")

    assert one_away("", "a")
    assert one_away("a", "")
    assert not one_away("", "aa")
    assert not one_away("aa", "")
    assert not one_away("", "aaaaaaa")
