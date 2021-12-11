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


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            grid = [[int(i) for i in row.strip()] for row in file]

        part1(grid)
