from string import ascii_lowercase, ascii_uppercase

def part1(data):
    nodes = {}
    for connection in data:
        pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            connections = [tuple(line.strip().split('-')) for line in file]
        print(connections)
