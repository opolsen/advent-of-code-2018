from d7 import solve_1, solve_2

INSTRUCTIONS = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
]


def test_solve_1():
    assert solve_1(INSTRUCTIONS) == 'CABDFE'


def test_solve_2():
    assert solve_2(INSTRUCTIONS, 2, 0) == 'CABFDE'
