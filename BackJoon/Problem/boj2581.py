import math

M = int(input())
N = int(input())

total = 0
minNum = 0
for i in range(M, N + 1):
    if i == 1:
        continue
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check:
        total += i
        if minNum == 0:
            minNum = i

if total == 0:
    print(-1)
else:
    print(total)
    print(minNum)
