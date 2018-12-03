import re
import numpy as np


def parse_claim(claim):
    split = re.split('[#@,:x]', claim)

    return {
        'id': int(split[1]),
        'left': int(split[2]),
        'top': int(split[3]),
        'width': int(split[4]),
        'height': int(split[5])
    }


def create_fabric(claims):
    fabric = np.zeros((max([c['height'] + c['left'] for c in claims]),
                       max([c['width'] + c['top'] for c in claims])),
                      dtype=np.int)

    for claim in claims:
        for i in range(claim['width']):
            for j in range(claim['height']):
                fabric[i + claim['left']][j + claim['top']] += 1

    return fabric


def solve_1(claims):
    parsed_claims = [parse_claim(claim) for claim in claims]

    fabric = create_fabric(parsed_claims)

    unique, counts = np.unique(fabric, return_counts=True)

    overlap_dict = dict(zip(unique, counts))

    overlaps = 0

    for key, value in overlap_dict.items():
        if key > 1:
            overlaps += value

    return overlaps


def solve_2(claims):
    parsed_claims = [parse_claim(claim) for claim in claims]

    fabric = create_fabric(parsed_claims)

    for claim in parsed_claims:
        overlaps = False
        for i in range(claim['width']):
            for j in range(claim['height']):
                if fabric[i + claim['left']][j + claim['top']] > 1:
                    overlaps = True
        if not overlaps:
            return claim['id']


if __name__ == '__main__':
    with open('input.txt') as f:
        claims = [line for line in f]

        print(f'solve_1: {solve_1(claims)}')
        print(f'solve_2: {solve_2(claims)}')
