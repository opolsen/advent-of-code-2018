from d3 import solve_1
from d3 import solve_2

CLAIMS = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]


def test_solve_1():
    assert solve_1(CLAIMS) == 4


def test_solve_2():
    assert solve_2(CLAIMS) == 3