def part1(data):
    """ bracket parsing """
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    paired  = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    solution = 0
    for line in data:
        open_brackets = []
        for bracket in line:
            if bracket in closers:
                expected = open_brackets.pop()
                if paired[expected] != bracket:
                    solution += score_table[bracket]
                    break
            elif bracket in openers:
                open_brackets.append(bracket)
    print(solution)
    # 370407


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            lines = [line.strip() for line in file]
    part1(lines)
