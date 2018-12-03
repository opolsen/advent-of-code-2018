import numpy as np


def solve_1(frequency_changes):
    return np.sum(frequency_changes)


def solve_2(frequency_changes):
    frequencies = {0}
    current_frequency = 0
    while True:
        for change in frequency_changes:
            resulting_frequency = current_frequency + change
            if resulting_frequency in frequencies:
                return resulting_frequency
            frequencies.add(resulting_frequency)
            current_frequency = resulting_frequency


if __name__ == '__main__':
    with open('input.txt') as f:
        frequency_changes = [int(line) for line in f]
        print(f'solve_1: {solve_1(frequency_changes)}')
        print(f'solve_2: {solve_2(frequency_changes)}')
