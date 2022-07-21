############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


n, m = [int(i) for i in input().split()]
world = inlt()


def solution(world, s, t, damage=0):
    if s < t:
        if world[s - 1] > world[s]:
            damage = damage + world[s - 1] - world[s]
        return solution(world, s + 1, t, damage)
    elif s > t:
        if world[s - 1] > world[s - 2]:
            damage = damage + world[s - 1] - world[s - 2]
        return solution(world, s - 1, t, damage)
    elif s == t:
        return damage


while m:
    s, t = [int(i) for i in input().split()]
    damage = 0
    print(solution(world, s, t, damage))

    m = m - 1
