import typing as tp
import itertools

Matrix:tp.TypeAlias = list[list[int]]

def zero_matrix(matrix: Matrix) -> Matrix:
    n = len(matrix)
    if n == 0:
        return matrix
    m = len(matrix[0])

    zero_rows = set()
    zero_columns = set()
    for i, j in itertools.product(range(n), range(m)):
        if matrix[i][j] == 0:
            zero_rows.add(i)
            zero_columns.add(j)

    for i, j in itertools.chain(
        itertools.product(zero_rows, range(m)),
        itertools.product(range(n), zero_columns),
    ):
        matrix[i][j] = 0
    return matrix


# ******************** Tests ********************


def test_zero_matrix() -> None:
    assert zero_matrix([]) == []
    assert zero_matrix([[1]]) == [[1]]
    assert zero_matrix([[0, 1]]) == [[0, 0]]
    assert zero_matrix([[1, 2, 3]]) == [[1, 2, 3]]
    assert zero_matrix(
        [
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
        ]
    ) == [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
    ]
    assert zero_matrix(
        [
            [1, 2, 3, 4],
            [1, 0, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
        ]
    ) == [
        [1, 0, 3, 4],
        [0, 0, 0, 0],
        [1, 0, 3, 4],
        [1, 0, 3, 4],
        [1, 0, 3, 4],
    ]
    assert zero_matrix(
        [
            [0, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 0],
        ]
    ) == [
        [0, 0, 0, 0],
        [0, 2, 3, 0],
        [0, 2, 3, 0],
        [0, 2, 3, 0],
        [0, 0, 0, 0],
    ]
    assert zero_matrix(
        [
            [1, 2, 3, 4],
            [1, 0, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 0],
            [1, 2, 3, 4],
        ]
    ) == [
        [1, 0, 3, 0],
        [0, 0, 0, 0],
        [1, 0, 3, 0],
        [0, 0, 0, 0],
        [1, 0, 3, 0],
    ]
    assert zero_matrix(
        [
            [0, 2, 3, 4],
            [0, 2, 3, 4],
            [0, 2, 3, 4],
            [0, 2, 3, 4],
            [0, 2, 3, 4],
        ]
    ) == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
