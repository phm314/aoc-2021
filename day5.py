def part1(data):
    sqsz = 1000
    grid = [[0 for y in range(sqsz)] for x in range(sqsz)]
    for line in data:
        x1, y1, x2, y2 = *line[0], *line[1]
        # ADD ONE range: [, ) -> [, ]
        if x1 == x2:
            for ypt in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][ypt] += 1
        if y1 == y2:
            for xpt in range(min(x1, x2), max(x1, x2) + 1):
                grid[xpt][y1] += 1

    solution = 0
    for row in grid:
        for pt in row:
            if pt > 1:
                solution += 1
   
    print(solution)
    # != 6802 (low)
    # == 6841

if __name__ == "__main__":
    import os
    os.system("cls")
    with open("inputs/day5.txt") as file:
        data = []
        for row in file:
            line = [[int(j) for j in i.split(",")] for i in row.strip().split(' -> ')]
            data.append(line)    
    part1(data)


