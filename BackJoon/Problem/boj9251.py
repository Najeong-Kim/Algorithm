import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()
check = [-1]
for i in range(len(second)):
    for j in reversed(range(len(check))):
        now = first[check[j] + 1:].find(second[i])
        if now == -1:
            continue
        else:
            now += max(0, check[j] + 1)
        if len(check) == j + 1:
            check.append(now)
        else:
            check[j + 1] = min(check[j + 1], now)

print(len(check) - 1)
