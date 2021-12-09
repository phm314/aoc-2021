def solve1(matrix):
    matrix = [[int(c) for c in row] for row in matrix]

    transposed_matrix = zip(*matrix)
    summed_rows = map(sum, transposed_matrix)
    majority = list(map(lambda s: s > len(matrix)//2, summed_rows))

    gamma   = ''.join('1' if b else '0' for b in majority)
    epsilon = ''.join('0' if b else '1' for b in majority)

    return int(gamma, 2) * int(epsilon, 2)


def solve2(matrix):
    matrix = [[int(c) for c in row] for row in matrix]

    def filter_down(m,inverse=False,i=0):
        if len(m) == 1:
            print(''.join(str(n) for n in m[0]))

            return ''.join(str(n) for n in m[0])

        else:
            transposed_m = zip(*m)

            for _ in range(i):
                next(transposed_m) #discarding what we don't need

            next_sum = sum(next(transposed_m))
            majority = next_sum >= len(m) / 2
            m = list(filter(lambda s: s[i] == int(majority != inverse), m))
            
            return filter_down(m,inverse,i+1)

    oxygen = filter_down(matrix)
    c02    = filter_down(matrix, inverse=True)

    return int(oxygen,2) * int(c02,2)
with open("inputs/day3.txt") as file:
    
    print(solve2([line.strip() for line in file]))
    # 2795310
