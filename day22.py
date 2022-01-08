import sys
import re

def part1(arg):
    cubes = []
    for c in arg:
        if c[1] >= -50 and c[2] <= 50:
            for d in cubes:
                intersect(c[1:], d[1:])
    return arg

def intersect(a, b):
    return a, b

with open(sys.argv[1]) as raw_data:
    lst = []
    for line in raw_data:
        mode = line.split()[0]
        data = map(int, re.findall(r"-?\d+", line))
        lst.append([mode, *data])
    part1(lst)
