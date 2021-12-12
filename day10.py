def part1(data):
    """ bracket parsing """
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    paired  = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_table1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score_table2 = {")": 1, "]":  2, "}":    3, ">":     4}
    solution1 = 0
    inc_scores = []
    for line in data:
        open_brackets = []
        for bracket in line:
            if bracket in closers:
                expected = open_brackets.pop()
                if paired[expected] != bracket:
                    solution1 += score_table1[bracket]
                    break
            elif bracket in openers:
                open_brackets.append(bracket)
        else:
            # part 2: incomplete lines
            score2 = 0
            for bracket2 in open_brackets[::-1]:
                score2 *= 5
                score2 += score_table2[paired[bracket2]]
            inc_scores.append(score2)
    inc_scores.sort()
    solution2 = inc_scores[len(inc_scores)//2]

    print(solution1)
    # 370407
    print(solution2)
    # 3249889609


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            lines = [line.strip() for line in file]
    part1(lines)
