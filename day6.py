def part1(initial):
    data = [i for i in initial]
    days = 80
    for day in range(days):
        print(day, len(data))
        new_units = 0
        for index in range(len(data)):
            if data[index] == 0:
                data[index] = 6
                new_units += 1
            else:
                data[index] -= 1
        if new_units:
            [data.append(8) for i in range(new_units)]

    print(len(data))
    # 386640

def part2(initial):
    groups = [0 for i in range(9)]
    for i in initial:
        groups[i] += 1
    days = 256

    for day in range(days):
        new_units = groups[0]
        for index in range(len(groups)):
            if index == 0:
                pass
            else:
                groups[index - 1] = groups[index]
                groups[index] = 0

        groups[8] = new_units
        groups[6] += new_units

        print(day, sum(groups))
        # != 1_878_664_243_379 (high)
        # == 1_733_403_626_279 

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("need file")    
    else:
        with open(sys.argv[1]) as file:
            data = [int(i) for i in file.read().split(',')]
        
        part2(data)

   
