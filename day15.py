import sys
from queue import PriorityQueue

def get_neighbors(ind, mx, my) -> list[tuple[int, int]]:
    neighbors = []
    x, y = ind
    if x > 0:
        neighbors.append((x - 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if x < mx - 1:
        neighbors.append((x + 1, y))
    if y < my - 1:
        neighbors.append((x, y + 1))
    return neighbors

def dijkstra(graph, source, edges):
    distances = {node: float("inf") for node in graph}
    queue = PriorityQueue()
    queue.put((graph[source], source))

    distances[source] = 0
    while not queue.empty():
        current = queue.get()
        neighbors = edges[current[1]]
        for neighbor in neighbors:
            distq = distances[current[1]] + graph[neighbor]
            if distq < distances[neighbor]:
                distances[neighbor] = distq
                queue.put((graph[neighbor], neighbor))
    return distances

with open(sys.argv[1]) as raw_data:
    grid = [[int(num) for num in line.strip()] for line in raw_data]

def solve(grid):
    gd = {(ny, nx): node for ny, row in enumerate(grid) for nx, node in enumerate(row)}
    nbrs = {node: get_neighbors(node, len(grid), len(grid[0])) for node in gd}
    src = (0, 0)
    solved = dijkstra(gd, src, nbrs)
    print(solved[(len(grid) - 1, len(grid[0]) - 1)])
    

def expand(matrix: list[list]) -> list[list]:
    result = []
    for i in range(5):
        for row in matrix:
            new_row = [x+i+j if x+i+j<10 else (x+i+j)%10+1 for j in range(5) for x in row]
            result.append(new_row)
    return result

# solve(grid)
# 673
large = expand(grid)
solve(large) # SLOW
# 2893

