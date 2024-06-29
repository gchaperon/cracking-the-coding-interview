
def urlify(value: list[str], length:int) -> list[str]:
    space_count = 0
    for i in range(length):
        if value[i] == " ":
            space_count += 1

    j = length + 2 * space_count - 1
    while j > i :
        if value[i] == " ":
            for c in "02%":
                value[j] = c
                j -= 1
            i -= 1
        else:
            value[j] = value[i]
            j -= 1
            i -= 1

    return value


# ******************** Tests ******************** 

def test_urlify_book() -> None:
    input_str = list("Mr 3ohn Smith") + [""] * 4
    output = urlify(input_str, 13)
    assert "".join(output) == "Mr%203ohn%20Smith"

def test_urlify_simple() -> None:
    input_str = list(" ") + [""] * 2
    output = urlify(input_str, 1)
    assert "".join(output) == "%20"
