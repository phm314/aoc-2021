def flatten(lst, common):
    v1, v2 = ("1", "0") if common else ("0", "1")
    for pos in range(len(lst[0])):
        val = 0

        # count value in position pos
        # could do both at the same time
        for elem in lst:
            val += (elem[pos] == "1")

        match = v1 if val >= 500 else v2
        inds = []
        for index, elem in enumerate(lst):
            if elem[pos] != match:
                inds.append(index)
        offset = 0
        for index in inds:
            if len(lst) == 1:
                return lst
            lst.pop(index-offset)
            offset += 1
    return lst

        

with open("inputs/day3.txt") as file:
    # part 1
    """
    count = []
    for line in file:
        for index, bit in enumerate(line.strip()):
            if index >= len(count):
                count.append(1)
            else:
                if bit:
                    count[index] += bit == "1"
    gamma = 0
    epsil = 0
    for amount in count:
        digit = amount > 500
        gamma = gamma * 10 + digit
        epsil = epsil * 10 + (not digit)
    int_g = int(f"{gamma}", 2)
    int_e = int(f"{epsil}", 2)
    print(int_g * int_e)
    
    # 12601314
    # 3148794
    """
    # part 2
    """
    LSR = OGR * CSR
    OGR = Most common bits
    CSR = Least common bits
    """
    numbers = []
    count = []
    for line in file:
        line = line.strip()
        numbers.append(line)
    gam, eps = numbers.copy(), numbers.copy()
    s1 = flatten(gam, 1)[0]
    s2 = flatten(eps, 0)[0]
    print(s1, s2)
    print(int(s1, 2) * int(s2, 2))
    # 3139560, 3140586, 4134816
