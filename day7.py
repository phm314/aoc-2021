def part1(data):
    solution = float("inf")
    for i in range(min(data), max(data)):
        current = 0
        for pos in data:
            current += abs(pos - i)
        if current < solution:
            solution = current

    # == 336131
    print(solution)
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("file")
    else:
        with open(sys.argv[1]) as file:
            data = [int(i) for i in file.read().split(',')]
        part1(data)
