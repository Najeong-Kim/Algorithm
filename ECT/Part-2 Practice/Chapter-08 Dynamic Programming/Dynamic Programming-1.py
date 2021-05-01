n = int(input())

d = [0] * 30001


def counter(a):
    min_num = 30000
    if a == 1:
        return True
    if a == 2 or a == 3 or a == 5:
        d[a] = 1
        return d[a]
    if d[a] != 0:
        return d[a]
    if d[a] == 0:
        if a % 2 == 0:
            min_num = min(counter(a//2), min_num)
        if a % 3 == 0:
            min_num = min(counter(a//3), min_num)
        if a % 5 == 0:
            min_num = min(counter(a//5), min_num)
        min_num = min(counter(a-1), min_num)
        d[a] = min_num + 1
        return d[a]


print(counter(n))
