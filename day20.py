import sys

def simulate(ref, init):
    # part 1 could probably be solved by padding the intial grid
    grid = pad_matrix(init, 1)
    # this first padding needs to be checked
    pad = 0
    # check whether infinite space will alternate
    flip = ref[0] == 1 and ref[-1] == 0
    # part 1: 2 steps, part 2: 50 steps
    for _ in range(50):
        grid = pad_matrix(grid, 1, int(pad))
        res = [x[:] for x in grid]
        for y in range(1, len(grid)-1):
            for x in range(1, len(grid[0])-1):
                current = []
                for ny, nx in neighbors(y, x):
                    current.append(grid[ny][nx])
                ind = int("".join(str(i) for i in current), 2)
                res[y][x] = ref[ind]
        grid = res
        if flip:
            # since we don't check edge cells, we need to flip them back
            grid = flip_edges(grid)
            pad = not pad
    print(count(grid))
    # part 1:
    # 5573, 5928 (high), 5357
    # 5503
    # part 2:
    # 19156

def flip_edges(arr):
    res = [x[:] for x in arr]
    for ind, row in enumerate(res):
        if ind in (0, len(arr) - 1):
            for ix, x in enumerate(row):
                res[ind][ix] = int(not x)
        else:
            row[0] = int(not x)
            row[-1] = int(not x)
    return res

def p_arr(arr):
    for row in arr:
        for x in row:
            ch = "#" if x else "."
            print(ch, end=" ")
        print()

def count(arr):
    res = sum(sum(row) for row in arr)
    return res

def neighbors(y, x):
    TL, TM, TR = (y-1, x-1), (y-1, x), (y-1, x+1)
    ML, MM, MR = (y, x-1), (y, x), (y, x+1)
    BL, BM, BR = (y+1, x-1), (y+1, x), (y+1, x+1)
    return [TL, TM, TR, ML, MM, MR, BL, BM, BR]

def pad_matrix(matrix, amount, fill=0):
    """ pads x * y list[list[]] with fill by amount in x, y directions """
    result = []
    len_r = len(matrix[0]) + amount * 2
    for row in matrix:
        new_row = [*[fill for _ in range(amount)],
                   *row,
                   *[fill for _ in range(amount)]]
        result.append(new_row)
    return [*[[fill for _ in range(len_r)] for _ in range(amount)],
            *result,
            *[[fill for _ in range(len_r)] for _ in range(amount)]]

with open(sys.argv[1]) as raw_data:
    algo, _, *string = [[1 if x == "#" else 0 for x in line.strip()] for line in raw_data]
    simulate(algo, string)
