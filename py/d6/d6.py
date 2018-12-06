from collections import defaultdict

import numpy as np


def calculate_manhattan_distance(coordinate, point):
    return abs(coordinate[0] - point[0]) + abs(coordinate[1] - point[1])


def create_grid(coordinates):
    grid = np.zeros((max([c[0] for c in coordinates]) + 1, max([c[1] for c in coordinates]) + 1), dtype=int)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            min_distance = grid.shape[0] * grid.shape[1]
            for idx, c in enumerate(coordinates):
                manhattan_distance = calculate_manhattan_distance(c, (i, j))
                if manhattan_distance < min_distance:
                    grid[i][j] = idx + 1
                    min_distance = manhattan_distance
                elif manhattan_distance == min_distance:
                    grid[i][j] = 0

    return grid


def find_edge_regions(grid):
    edge_regions = set()

    for i in range(grid.shape[0]):
        edge_regions.add(grid[i][0])
        edge_regions.add(grid[i][grid.shape[1] - 1])

    for j in range(grid.shape[1]):
        edge_regions.add(grid[0][j])
        edge_regions.add(grid[grid.shape[0] - 1][j])

    return edge_regions


def solve_1(coordinates):
    grid = create_grid(coordinates)

    edges = find_edge_regions(grid)

    d = defaultdict(int)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            d[grid[i][j]] += 1

    return max([v for k, v in d.items() if k not in edges])


def is_within_region(coordinates, point, distance):
    return sum([calculate_manhattan_distance(coordinate, point) for coordinate in coordinates]) < distance


def solve_2(coordinates, distance):
    grid = create_grid(coordinates)

    safe_region_size = 0

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if is_within_region(coordinates, (i, j), distance):
                safe_region_size += 1

    return safe_region_size


if __name__ == '__main__':
    with open('input.txt') as f:
        coordinates = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in f]
        print(f'solve_1: {solve_1(coordinates)}')
        print(f'solve_2: {solve_2(coordinates, 10000)}')
