from d1 import solve_1, solve_2


def test_1():
    assert solve_1([1, 1, 1]) == 3
    assert solve_1([1, 1, -2]) == 0
    assert solve_1([-1, -2, -3]) == -6


def test_2():
    assert solve_2([1, -1]) == 0
    assert solve_2([3, 3, 4, -2, -4]) == 10
    assert solve_2([-6, 3, 8, 5, -6]) == 5
    assert solve_2([7, 7, -2, -7, -4]) == 14
