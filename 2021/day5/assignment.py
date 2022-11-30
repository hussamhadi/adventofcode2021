# coding=utf-8
"""
 Advent of code
"""
from collections import defaultdict
all_lines = []
with open('input.txt', 'r') as input:
    for x, line in enumerate(input):
        coords = line.replace('\n', '').split(' -> ')
        all_lines.append([])
        for coord in coords:
            point = map(int, coord.split(','))
            all_lines[x].append(tuple(point))


def assignment(diagonal=False):
    points = defaultdict(int)
    for line in all_lines:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            if not diagonal:
                continue
            dx = 1 if line[0][0] < line[1][0] else -1
            dy = 1 if line[0][1] < line[1][1] else -1
            for i, x in enumerate(range(line[0][0], line[1][0] + dx, dx)):
                y = line[0][1] + i * dy
                point = (x, y)
                points[point] += 1

        if line[0][0] == line[1][0]:
            # vertical line
            # sort coordinates from low to high if needed
            if line[0][1] > line[1][1]:
                line = list(reversed(line))
            for i in range(line[0][1], line[1][1]+1):
                point = (line[0][0], i)
                points[point] += 1
        if line[0][1] == line[1][1]:
            # sort coordinates from low to high if needed
            if line[0][0] > line[1][0]:
                line = list(reversed(line))
            for i in range(line[0][0], line[1][0]+1):
                point = (i, line[0][1])
                points[point] += 1

    thick_points = [k for k, v in points.items() if v > 1]
    print(len(thick_points))


if __name__ == '__main__':
    assignment()
    assignment(diagonal=True)
