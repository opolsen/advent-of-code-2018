from d6 import solve_1, solve_2


COORDINATES = [
    (1, 1),
    (1, 6),
    (8, 3),
    (3, 4),
    (5, 5),
    (8, 9)
]


def test_solve_1():
    assert solve_1(COORDINATES) == 17


def test_solve_2():
    assert solve_2(COORDINATES, 32) == 16