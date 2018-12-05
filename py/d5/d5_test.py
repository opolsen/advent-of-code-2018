from d5 import solve_1, solve_2


POLYMER = 'dabAcCaCBAcCcaDA'


def test_solve_1():
    assert solve_1(POLYMER) == 10


def test_solve_2():
    assert solve_2(POLYMER) == 4