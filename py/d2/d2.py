import numpy as np


def count_char(id, char):
    return np.sum([1 if c == char else 0 for c in id])


def solve_1(ids):
    two_count = 0
    three_count = 0

    for id in ids:
        has_two_count = False
        has_three_count = False
        for c in {c for c in id}:
            if count_char(id, c) == 2:
                has_two_count = True
            if count_char(id, c) == 3:
                has_three_count = True
        if has_two_count:
            two_count += 1
            has_two_count = False
        if has_three_count:
            three_count += 1
            has_three_count = False
    return two_count * three_count


def difference(id_a, id_b):
    diff = 0
    for i in range(len(id_a)):
        if id_a[i] != id_b[i]:
            diff += 1
    return diff


def common(id_a, id_b):
    common = ''
    for i in range(len(id_a)):
        if id_a[i] == id_b[i]:
            common += id_a[i]
    return common


def solve_2(ids):
    min_diff_value = len(ids[0])
    min_diff_ids = (ids[0], ids[1])
    for id_a in ids:
        for id_b in ids:
            if id_a != id_b:
                diff = difference(id_a, id_b)
                if diff < min_diff_value:
                    min_diff_value = diff
                    min_diff_ids = (id_a, id_b)
    return common(min_diff_ids[0], min_diff_ids[1])


if __name__ == '__main__':
    with open('input.txt') as f:
        IDs = [line for line in f]
        print(f'solve_1: {solve_1(IDs)}')
        print(f'solve_2: {solve_2(IDs)}')
