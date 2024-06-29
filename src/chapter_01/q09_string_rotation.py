def is_substring(word: str, string:str) -> bool:
    return word in string

def is_rotation(s1: str, s2:str) -> bool:
    return is_substring(s1, s2 + s2)


# ******************** Tests ********************
def test_is_rotation() -> None:
    assert is_rotation("waterbottle", "erbottlewat")
    assert not is_rotation("hi", "bye")
