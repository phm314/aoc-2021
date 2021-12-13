def find_all_unique_paths(nodes):
    start_node = "start"
    return search_node(nodes, start_node)

def search_node(nodes, *path):
    node = path[-1]
    if node == "end":
        yield path
    for destination in nodes[node]:
        if destination.islower() and destination not in path or not destination.islower():
            yield from search_node(nodes, *path, destination)

def search_node2(nodes, *path):
    node = path[-1]
    if node == "end":
        yield path
        # returning here seems to stop iteration, unlike in search1
        return
    small = [cave for cave in path if cave.islower()]
    if len(small) == len(set(small)):
        has_doubled = False
    else:
        has_doubled = True

    for destination in nodes[node]:
        # can visit a small cave twice: so we can check every search if we've done so
        if has_doubled:
            if destination.islower() and destination not in path \
                or not destination.islower():
                yield from search_node2(nodes, *path, destination)

        else:
            yield from search_node2(nodes, *path, destination)

def finder2(nodes):
    start = "start"
    return search_node2(nodes, start)

def part1(data):
    nodes = {}
    for conn in data:
        for node in conn:
            if node not in nodes:
                nodes[node] = []
        if conn[1] != "start":
            nodes[conn[0]].append(conn[1])
        if conn[0] != "start":
            nodes[conn[1]].append(conn[0])

    gen = find_all_unique_paths(nodes)
    solution1 = 0
    for path in gen:
        solution1 += 1
    print(solution1)
    # 3000

def part2(data):
    nodes = {}
    for conn in data:
        for node in conn:
            if node not in nodes:
                nodes[node] = []
        if conn[1] != "start":
            nodes[conn[0]].append(conn[1])
        if conn[0] != "start":
            nodes[conn[1]].append(conn[0])

    gen = finder2(nodes)
    solution2 = 0
    for path in gen:
        solution2 += 1
    # 74222
    print(solution2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            connections = [tuple(line.strip().split('-')) for line in file]
        part2(connections)
