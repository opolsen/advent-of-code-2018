import re
from collections import defaultdict


def parse_record(record):
    split = re.split('[\\[\\]]', record)

    return {
        'timestamp': split[1],
        'command': split[2]
    }


def parse_id(command):
    return int(command.split('#')[1].split('begins')[0])


def create_timeline(records):
    sleep_times = []

    guard_id = None
    asleep_start = None

    for record in sorted(records, key=lambda r: r['timestamp']):
        if 'Guard' in record['command']:
            guard_id = parse_id(record['command'])
        if 'asleep' in record['command']:
            asleep_start = record['timestamp']
        if 'wakes up' in record['command']:
            sleep_times.append((guard_id, asleep_start, record['timestamp']))

    return sleep_times


def parse_minute(timestamp):
    return int(timestamp.split(':')[1])


def find_most_asleep_guard(timeline):
    total_sleep_per_guard = defaultdict(int)

    for record in timeline:
        total_sleep_per_guard[record[0]] += (parse_minute(record[2]) - parse_minute(record[1]))

    max_guard_id = -1
    max_total_sleep = -1

    for guard_id, total_sleep in total_sleep_per_guard.items():
        if total_sleep > max_total_sleep:
            max_guard_id = guard_id
            max_total_sleep = total_sleep

    return max_guard_id


def find_most_frequent_sleep_minute(timeline, guard_id):
    sleep_frequency = [0] * 60

    for record in timeline:
        if record[0] == guard_id:
            for i in range(parse_minute(record[1]), parse_minute(record[2])):
                sleep_frequency[i] += 1

    max_minute = -1
    max_frequency = -1

    for minute, frequency in enumerate(sleep_frequency):
        if frequency > max_frequency:
            max_frequency = frequency
            max_minute = minute

    return max_minute, max_frequency


def solve_1(records):
    parsed_records = [parse_record(record) for record in records]

    timeline = create_timeline(parsed_records)

    guard_id = find_most_asleep_guard(timeline)

    minute, _ = find_most_frequent_sleep_minute(timeline, guard_id)

    return guard_id * minute


def solve_2(records):
    parsed_records = [parse_record(record) for record in records]

    timeline = create_timeline(parsed_records)

    ids = {record[0] for record in timeline}

    max_minute = -1
    max_frequency = -1
    max_id = -1

    for id in ids:
        minute, frequency = find_most_frequent_sleep_minute(timeline, id)
        if frequency > max_frequency:
            max_frequency = frequency
            max_minute = minute
            max_id = id

    return max_id * max_minute


if __name__ == '__main__':
    with open('input.txt') as f:
        records = [line for line in f]
        print(f'solve_1: {solve_1(records)}')
        print(f'solve_2: {solve_2(records)}')
