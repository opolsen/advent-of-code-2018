def perform_reactions(polymer):
    current = ''
    skip = False
    while True:
        for i in range(len(polymer) - 1):
            if skip:
                skip = False
                if i == len(polymer) - 2:
                    current += polymer[i + 1]
            elif polymer[i].lower() == polymer[i + 1].lower() and polymer[i] != polymer[i + 1]:
                skip = True
            else:
                current += polymer[i]
                if i == len(polymer) - 2:
                    current += polymer[i + 1]

        if current == polymer:
            return len(current)
        else:
            polymer = current
            current = ''
            skip = False


def remove_type(letter, polymer):
    new_polymer = ''
    for c in polymer:
        if c.lower() != letter:
            new_polymer += c
    return new_polymer


def solve_1(polymer):
    return perform_reactions(polymer)


def solve_2(polymer):
    return min([perform_reactions(remove_type(type, polymer)) for type in 'abcdefghijklmnopqrstuvwxyz'])


if __name__ == '__main__':
    with open('input.txt') as f:
        polymer = [line for line in f][0]
        print(f'solve_1: {solve_1(polymer)}')
        print(f'solve_2: {solve_2(polymer)}')