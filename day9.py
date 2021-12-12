def part1(data):
    """
    check both directions by rotating array, then rotate it back.
    solution is found from r && c.
    """
    data_rotated = []
    for i in range(len(data[0])):
        row = []
        for j, _ in enumerate(data):
            row.append(data[j][i])
        data_rotated.append(row)

    boolsr = find_lowpoint_1d(data)
    boolsc = find_lowpoint_1d(data_rotated)
    boolsc_rot = []

    for i in range(len(boolsc[0])):
        row = []
        for j, _ in enumerate(boolsc):
            row.append(boolsc[j][i])
        boolsc_rot.append(row)

    final_arr = [[1 if boolsr[j][i] and boolsc_rot[j][i] else 0 \
            for i in range(len(data[0]))] for j in range(len(data))]

    solution = 0
    for row_ind, row in enumerate(final_arr):
        for col_ind, col in enumerate(row):
            if col:
                solution += data[row_ind][col_ind] + 1
    print(solution)
    # == 514


def find_lowpoint_1d(lst):
    """ finds singular lowest point in a simple list. """
    large = [[0 for i in row] for row in lst]
    for row_ind, test in enumerate(lst):

        sol_inds = []
        for ind, num in enumerate(test):
            # trace every starting point maybe?
            # until it reaches a low point [p < n1 && p < n2]
            # else check next point in same direction...

            nxt = []
            if ind != (len(test) - 1):
                nxt.append(ind + 1)
            if ind != 0:
                nxt.append(ind - 1)

            pts = []
            for nxt_ind in nxt:
                if test[nxt_ind] < num:
                    pts.append(nxt_ind)
                elif test[nxt_ind] == num:
                    # appends to end of current array, making sure that
                    # nxt_ind exists
                    to_app = nxt_ind + (-1 if nxt_ind < ind else 1)
                    if 0 <= to_app <= len(test) - 1:
                        nxt.append(to_app)

            if len(pts) == 0:
                sol_inds.append(ind)
        for sol_ind in sol_inds:
            large[row_ind][sol_ind] = 1
    return large

def part2(data):
    """
    every square that is not a 9 forms a basin,
    so we can search through those. basically,
    solving part 2 with the same iterative method.
    """
    basin_data = [[int(elem != 9) for elem in row] for row in data]
    all_basins = []
    for r_ind, row in enumerate(basin_data):
        for c_ind, col in enumerate(row):
            if not col:
                continue
            neighbors = []
            if r_ind != 0:
                neighbors.append((r_ind - 1, c_ind))
            if r_ind != len(basin_data) - 1:
                neighbors.append((r_ind + 1, c_ind))
            if c_ind != 0:
                neighbors.append((r_ind, c_ind - 1))
            if c_ind != len(row) - 1:
                neighbors.append((r_ind, c_ind + 1))

            current_basin = []
            for rnxt, cnxt in neighbors:
                if not basin_data[rnxt][cnxt]:
                    continue
                current_basin.append((rnxt, cnxt))
                basin_data[rnxt][cnxt] = 0
                # add next neighbors to check in current list

                if rnxt != 0:
                    neighbors.append((rnxt - 1, cnxt))
                if rnxt != len(basin_data) - 1:
                    neighbors.append((rnxt + 1, cnxt))
                if cnxt != 0:
                    neighbors.append((rnxt, cnxt - 1))
                if cnxt != len(row) - 1:
                    neighbors.append((rnxt, cnxt + 1))

            all_basins.append(current_basin)

    all_basins.sort(reverse=True, key=len)
    solution = len(all_basins[0]) * len(all_basins[1]) * len(all_basins[2])
    print(solution)
    # 1103130

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            grid = [[int(i) for i in row.strip()] for row in file]

        part2(grid)
