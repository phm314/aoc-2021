with open("inputs/day2.txt") as file:
    # part 1
    """
    posy = 0
    posx = 0
    for line in file:
        direction, amount = line.split()
        # print(amount, direction)
        dn = int(amount)
        if direction == "forward":
            posx += dn
        elif direction == "up":
            posy -= dn
        elif direction == "down":
            posy += dn
    print(posy, posx)
    print(posy * posx)

    #2239912
    """
    # part 2
    aim = 0
    posx, posy = 0, 0

    for line in file:
        direction, amount = line.split()
        dn = int(amount)
        if direction == "down":
            aim += dn
        elif direction == "up":
            aim -= dn
        elif direction == "forward":
            posx += dn
            posy += (aim * dn)
    print(posx * posy)
    # 1942068080
