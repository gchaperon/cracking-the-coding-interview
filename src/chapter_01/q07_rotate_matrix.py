import itertools
import functools
import typing as tp

Matrix: tp.TypeAlias = list[list[int]]


def rot(i: int, j: int, n: int) -> tuple[int, int]:
    """Rotate a single coordinate."""
    return j, n - i - 1


def ceildiv(m: int, n: int) -> int:
    """Integer division, but rounded up."""
    return (m + n - 1) // n

def rotate_matrix(matrix: Matrix) -> Matrix:
    n = len(matrix)
    rot_ = functools.partial(rot, n=n)

    for i, j in itertools.product(range(ceildiv(n, 2)), range(n // 2)):
        corners = []
        values = []
        for _ in range(4):
            corners.append((i, j))
            values.append(matrix[i][j])
            i, j = rot_(i, j)

        for (i, j), value in zip(corners, [values[-1], *values[:-1]]):
            matrix[i][j] = value
    return matrix


# ******************** Tests ********************

def test_rot() -> None:
    assert rot(0, 0, 1) == (0, 0)
    assert rot(0, 0, 2) == (0, 1)
    assert rot(1, 1, 2) == (1, 0)
    assert rot(1, 1, 3) == (1, 1)
    assert rot(2, 1, 3) == (1, 0)
    assert rot(1, 0, 4) == (0, 2)
    assert rot(2, 3, 4) == (3, 1)

def test_rotate_matrix() -> None:
    assert rotate_matrix([]) == []
    assert rotate_matrix([[3]]) == [[3]]
    assert rotate_matrix(
        [
            [1, 2],
            [3, 4],
        ]
    ) == [
        [3, 1],
        [4, 2],
    ]
    assert rotate_matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    ) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    assert rotate_matrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    ) == [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]
    assert rotate_matrix(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
    ) == [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]
