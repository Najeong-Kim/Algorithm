import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

check = [[-1, '']]

for i in range(len(second)):
    for j in reversed(range(len(check))):
        now = first[check[j][0] + 1:].find(second[i])
        if now == -1:
            continue
        else:
            now += max(0, check[j][0] + 1)
        if len(check) == j + 1:
            check.append([now, check[j][1] + first[now]])
        else:
            if check[j + 1][0] > now:
                check[j + 1] = [now, check[j][1] + first[now]]

if len(check) == 1:
    print(0)
else:
    print(len(check) - 1)
    print(check[-1][1])
