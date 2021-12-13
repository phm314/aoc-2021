def part1(points, folds):
    # part 1 only first fold
    for plane, fold in folds:
        if plane == "y":
            ind = 1
        else:
            ind = 0
        for point in points:
            if point[ind] > fold:
                point[ind] = fold - (point[ind] - fold)

    m_x = max((p[0] for p in points)) + 1
    m_y = max((p[1] for p in points)) + 1
    grid = [[0 for x in range(m_x)] for y in range(m_y)]
    for x, y in points:
        grid[y][x] = 1

    solution1 = 0
    # solution 2:
    # KJBKEUBG
    for row in grid:
        for item in row:
            val = 0 if item else "."
            print(val, end = " ")
            if item: solution1 += 1
        print()

    # print(solution1)
    # 788

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            pts = []
            foldlns = []
            flag = 0
            for line in file:
                line = line.strip()
                if line:
                    if flag:
                        foldlns.append(line)
                    else:
                        pts.append(line)

                else:
                    flag = 1
        pts = [list(map(int, point.split(","))) for point in pts]
        foldlns = [fold.split("fold along ")[1].split("=") for fold in foldlns]
        foldlns = [(fold[0], int(fold[1])) for fold in foldlns]

        part1(pts, foldlns)
