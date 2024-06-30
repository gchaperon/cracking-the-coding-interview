def palindrome_permutation(value: str) -> bool:
    """Checks if the input is a permutation of a palindrome.

    Ignores case and whitespace in input.

    Palindromes have even count of characters, except when the length of the
    word is odd, in which case there must be one character that has odd
    count.
    """
    sanitized = [c.lower() for c in value if c != " "]

    def is_even(n: int) -> bool:
        return n % 2 == 0

    def counter(string: list[str]) -> dict[str, int]:
        out: dict[str, int] = {}
        for c in string:
            if c in out:
                out[c] += 1
            else:
                out[c] = 1
        return out

    char_count = counter(sanitized)
    if is_even(len(sanitized)):
        return all(is_even(count) for count in char_count.values())
    else:
        odd_count = sum(not is_even(count) for count in char_count.values())
        return odd_count == 1


# ******************** Tests ********************


def test_palindrome_permutation() -> None:
    assert palindrome_permutation("Tact Coa")
    assert palindrome_permutation("a")
    assert palindrome_permutation("aabbccd")

    assert not palindrome_permutation("abc")
    assert not palindrome_permutation("aaabbc")
