from d2 import solve_1, solve_2

IDS_1 = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab'
]


def test_solve_1():
    assert solve_1(IDS_1) == 12


IDS_2 = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz'
]


def test_solve_2():
    assert solve_2(IDS_2) == 'fgij'
