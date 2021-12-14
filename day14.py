from collections import Counter, defaultdict
import copy

def part1(template, rules):
    # part 1: 10, part 2: 40
    steps = 10
    for _ in range(steps):
        ntpl = []
        for ind in range(len(template) - 1):
            pair = template[ind: ind + 2]
            to_ins = rules[pair]
            ntpl.append(template[ind])
            ntpl.append(to_ins)
        ntpl.append(template[-1])
        template = "".join(ntpl)
    counter = Counter(template)
    print(counter)
    # print(max(counter.values()) - min(counter.values()))
    # 2408

def part2(template, rules):
    # with help from:
    # https://github.com/womogenes/AoC-2021-Solutions/blob/main/day_14/day_14_p2.py
    freqs = defaultdict(int)
    for i in range(len(template) - 1):
        freqs[template[i:i + 2]] += 1

    for i in range(40):
        freqs = replace(freqs, rules)

    counter = defaultdict(int)
    for pair in freqs:
        counter[pair[0]] += freqs[pair]
        counter[pair[1]] += freqs[pair]

    counter[template[0]] += 1
    counter[template[-1]] += 1
    # only take half from counted values?
    count_vals = [c // 2 for c in counter.values()]
    solution2 = max(count_vals) - min(count_vals)

    print(solution2)
    # 2651311098752

def replace(freqs, rules):
    new_freqs = copy.copy(freqs)
    for pair in freqs:
        for start, end in rules:
            if pair == start:
                occs = freqs[pair]
                new_freqs[pair] -= occs
                new_freqs[pair[0] + end] += occs
                new_freqs[end + pair[1]] += occs
                break

    return new_freqs


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            lines = [line.strip() for line in f]
        polymer = lines[0]
        insertion = [line.split(" -> ") for line in lines[2:]]

        #part1(polymer, insertion)
        part2(polymer, insertion)
