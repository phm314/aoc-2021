import os
os.system("clear")
with open("inputs/day1.txt") as file:

    # day 1: 
    """
    sol1 = 0
    last = 0
    for line in file:
        num = int(line)
        if last and num > last:
            sol1 += 1
        last = num
    print(sol1)
    """
    # == 1466

    # day 2:
    wsize = 3
    nums = [int(line) for line in file]
    sums = [sum(nums[ind:ind+wsize])for ind in range(len(nums) - wsize)]
    
    sol2 = 0
    last = 0
    for item in sums:
        if item > last:
            sol2 += 1
        last = item
    print(sums)
    print(sol2)
    # != 1490
    # == 1490

