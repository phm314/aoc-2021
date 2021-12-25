import sys

def part1(data):
    # with help from
    # https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hps5hgw
    x = 0
    bfr = [[], [], []]
    stack = []
    for ind, line in enumerate(data):
        if x == 4:
            bfr[0].append(int(line[2]))
        elif x == 5:
            bfr[1].append(int(line[2]))
        elif x == 15:
            bfr[2].append(int(line[2]))

        if not ind % 18:
            x = 0
        x+=1
    for x in range(14):
        print(f"{x:3d}", end=" ")
    print()
    for x in bfr:
        for i in x:
            print(f"{i:3d}", end=" ")
        print()

    for ind, num in enumerate(bfr[0]):
        if num == 1:
            stack.append(ind)
        elif num == 26:
            m = stack.pop()
            print(m, ind, bfr[2][m] + bfr[1][ind])
    # part 1:
    # 92969593497992
    # part 2:
    # 81514171161381


with open(sys.argv[1]) as raw_data:
    lines = [line.strip().split() for line in raw_data]
    part1(lines)
