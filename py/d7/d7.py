def parse(instruction):
    split = instruction.split('Step ')[1].split(' must')
    return (split[0], split[1].split('step ')[1].split(' can')[0])


def find_all_instructions(instruction_orders):
    instructions = set()
    for before, after in instruction_orders:
        instructions.add(before)
        instructions.add(after)
    return instructions


def solve_1(instructions):
    parsed = [parse(instruction) for instruction in instructions]

    total_instructions = find_all_instructions(parsed)

    order = ''

    while len(order) < len(total_instructions):
        for c in sorted(total_instructions):
            if c in order:
                continue

            is_next = True

            for x, y in parsed:
                if y == c and x not in order:
                    is_next = False

            if is_next:
                order += c
                break

    return order


def initialize_workers(worker_count):
    workers = []
    for i in range(worker_count):
        workers.append((None, 0, True))  # (instruction, started, ready)
    return workers


def has_available_worker(workers):
    return any([available for _, _, available in workers])


def available_worker_index(workers):
    for i, w in enumerate(workers):
        if w[2]:
            return i


def is_worked_on(c, workers):
    return any([True if instruction == c else False for instruction, _, _ in workers])


def solve_2(instructions, worker_count, duration):
    parsed = [parse(instruction) for instruction in instructions]

    workers = initialize_workers(worker_count)

    total_instructions = find_all_instructions(parsed)

    tick = 0
    order = ''

    while len(order) < len(total_instructions):
        finished_instructions = []

        for i, w in enumerate(workers):
            if not w[2] and w[1] + duration + ord(w[0]) - 64 == tick:
                finished_instructions.append(w[0])
                workers[i] = (None, tick, True)

        if finished_instructions:
            print(f'finished instructions: {finished_instructions}')

        for u in sorted(finished_instructions):
            order += u

        for instruction in sorted(total_instructions):
            if instruction in order:
                continue

            can_start = True

            for before, after in parsed:
                if after == instruction and before not in order:
                    can_start = False

            if can_start and not is_worked_on(instruction, workers) and has_available_worker(workers):
                workers[available_worker_index(workers)] = (instruction, tick, False)

        tick += 1

    return order


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = [line for line in f]
        print(f'solve_1: {solve_1(instructions)}')
        print(f'solve_2: {solve_2(instructions, 5, 60)}')