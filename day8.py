def part1(data):
    solution = 0
    for line in data:
        for word in line[1]:
            if len(word) in (2, 4, 3, 7):
                solution += 1

    print(solution)
    # != 260 (low)
    # == 352

def solve(segments):
    # solving seven segment display mixup
    knowndigits = {}
    knownsegments = {}
    len5 = []
    len6 = []


    # parsing list exclusive sets into solvable sets
    for unknown in segments:
        if len(unknown) == 2:
            knowndigits[1] = unknown
        elif len(unknown) == 3:
            knowndigits[7] = unknown
        elif len(unknown) == 4:
            knowndigits[4] = unknown
        elif len(unknown) == 7:
            knowndigits[8] = unknown
        elif len(unknown) == 5:
            len5.append(unknown)
        elif len(unknown) == 6:
            len6.append(unknown)

    # method

    for set_ in len5:
        if len(knowndigits[1] & set_) == 2:
            knowndigits[3] = set_
            len5.remove(set_)
            break

    for set_ in len6:
        if len(set_ - knowndigits[3]) == 1:
            knowndigits[9] = set_
            len6.remove(set_)
            break

    for set_ in len5:
        if len(knowndigits[9] - set_) == 1:
            knowndigits[5] = set_
            knownsegments['c'] = ''.join(knowndigits[9] - set_)
            len5.remove(set_)
            break

    for set_ in len6:
        if knownsegments['c'] in set_:
            knowndigits[0] = set_
            len6.remove(set_)
            knowndigits[6] = len6.pop()
            break

    knowndigits[2] = len5.pop()
    return knowndigits


def part2(data):
    solution = 0
    for line in data:
        current = 0
        segments, output = line
        segments = [set(i) for i in segments]
        solved = solve(segments)
        rev = {frozenset(set_): num for num, set_ in solved.items()}
        for out_seg in output:
            num_set = frozenset(out_seg)
            current *= 10
            current += rev[num_set]
        solution += current
    print(solution)
    # 936117

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("file")
    else:
        with open(sys.argv[1]) as file:
            data = [[word.split() for word in line.strip().split(" | ")] for line in file]
            
        part2(data)
