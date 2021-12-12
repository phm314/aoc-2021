def printgrid(data):
    for row in data:
        for item in row:
            color = "\33[38;5;9m" if not item else "" if item != 9 else "\33[38;5;6m"
            endf = "\33[0m"
            print(color, item, endf, sep = "", end = " ")
        print()

def calculate_neighbor_inds(r_ind, c_ind, rsz, csz):
    """ returns tuple(int, int) of index for all adjacent,
    and diagonal squares"""
    result = []
    if r_ind != 0:
        # N
        result.append((r_ind - 1, c_ind))
        if c_ind != 0:
            # NW
            result.append((r_ind - 1, c_ind - 1))
        if c_ind != csz - 1:
            # NE
            result.append((r_ind - 1, c_ind + 1))
    if r_ind != rsz - 1:
        # S
        result.append((r_ind + 1, c_ind))
        if c_ind != 0:
            # SW
            result.append((r_ind + 1, c_ind - 1))
        if c_ind != csz - 1:
            # SE
            result.append((r_ind + 1, c_ind + 1))
    if c_ind != 0:
        # W
        result.append((r_ind, c_ind - 1))
    if c_ind != csz - 1:
        # E
        result.append((r_ind, c_ind + 1))

    return result

def part1(data):
    steps = 1000
    # do step:
    neighbor_inds = [[calculate_neighbor_inds(j, i, len(data), len(row)) \
                for i, elem in enumerate(row)] \
                for j, row in enumerate(data)]
    solution1 = 0
    for step in range(steps):

        inter = [[i + 1 if i != 9 else 0 for i in row] for row in data]
        stepglow = 0
        # every squares gains 1 each step
        zeros = []
        for r_ind, row in enumerate(inter):
            for c_ind, item in enumerate(row):
                # squares that would reach 10 glow, resetting to 0
                """
                value = item + 1 if item != 9 else 0
                inter[r_ind][c_ind] = value
                """
                if not item:
                    stepglow += 1
                    zeros.append((r_ind, c_ind))

        # start by checking all squares of 0's neighbors
        for zr_ind, zc_ind in zeros:
            for nzr, nzc in neighbor_inds[zr_ind][zc_ind]:
                item = inter[nzr][nzc]
                # neighbor already glowing
                if item == 0:
                    continue
                value = item + 1 if item != 9 else 0
                inter[nzr][nzc] = value
                if not value:
                    stepglow += 1
                    zeros.append((nzr, nzc))

        solution1 += stepglow
        # part 2 : simul glow
        if stepglow == 100:
            print(step + 1)
            return

        data = inter
        # part 1
        print(stepglow, solution1)
        # 1632


if __name__ == "__main__":
    import sys
    import os
    os.system("color")
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            grid = [[int(i) for i in line.strip()] for line in file]
        part1(grid)
