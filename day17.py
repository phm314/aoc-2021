import sys

def step(pos, vel):
    pos[0] += vel[0]
    pos[1] += vel[1]
    vel = max(vel[0] - 1, 0), vel[1] - 1
    return pos, vel

def collision(pos, tar):
    """ check for collision, or if target has been passed """
    x, y = pos
    (txmin, txmax), (tymin, tymax) = tar
    if x > txmax or y < tymax:
        return -1
    if x < txmin or y > tymin:
        return 0
    return 1

def main(arg):
    with open(arg, "r") as raw_data:
        square = raw_data.read().split()
        sx = list(map(int, square[2][2:].strip(",").split("..")))
        sy = list(map(int, square[3][2:].split("..")))[::-1]
        target = [sx, sy]
        #target = [20, 30], [-5, -10]  # test case : 45, 112
    maxy = 0
    distinct_initial_velocities = 0
    print(target)
    for vx in range(target[0][1] + 1):
        for vy in range(target[1][1] - 1, 180):
            tentativey = 0
            position = [0, 0]
            velocity = [vx, vy]
            hit = 0
            while (hit not in [1, -1]) or \
                    (velocity[0] == 0 and target[0][1] < position[0] < target[0][0]):
                    # no x velocity & not above target
                position, velocity = step(position, velocity)
                tentativey = max(position[1], tentativey)
                hit = collision(position, target)
            if hit == 1:
                distinct_initial_velocities += 1
                maxy = max(maxy, tentativey)

    print(maxy)
    # 105 (low)
    # 11781
    print(distinct_initial_velocities)
    # ? 228 , 913, 4315, 4369, 4531
    # 4531
main(sys.argv[1])
