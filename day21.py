import sys
import functools

def part1(*starts):
    score = [0 for i in starts]
    pos = [board_gen(1, 11) for x in starts]
    for ind, it in enumerate(pos):
        for _ in range(starts[ind]):
            next(it)
    turn = 0
    die = loaded(1, 101)
    rollcount = 0
    while score[0] < 1000 and score[1] < 1000:
        distance = next(die) + next(die) + next(die)
        rollcount += 3
        dest = [next(pos[turn]) for x in range(distance)][-1]
        score[turn] += dest
        turn = not turn
        print(turn, score)
    solution1 = rollcount * score[turn]
    print(solution1)
    # 798147

def loaded(start, end):
    while True:
        yield from range(start, end)

def board_gen(start, end):
    while True:
        yield from range(start, end)

def part2(*starts):
    scores = 0, 0
    result = dirac(starts[0]-1, starts[1]-1, *scores)
    print(result)
    print(max(result))
    # 716241959649754 (low, other's answer)
    # 809953813657517 (int - 1)

roll_sums = {3: 1,
             4: 3,
             5: 6,
             6: 7,
             7: 6,
             8: 3,
             9: 1}

@functools.lru_cache(maxsize=None)
def dirac(apos, bpos, ascr, bscr):
    if ascr >= 21:
        return 1, 0
    if bscr >= 21:
        return 0, 1
    attl, bttl = 0, 0
    for dsum, damt in roll_sums.items():
        npos = (apos + dsum) % 10
        nscr = ascr + npos + 1
        bwin, awin = dirac(bpos, npos, bscr, nscr)
        attl += awin * damt
        bttl += bwin * damt
    return attl, bttl

with open(sys.argv[1]) as raw_data:
    args = [int(line.strip()[-1]) for line in raw_data]
#args = [4, 8]
#part1(*args)
part2(*args)
