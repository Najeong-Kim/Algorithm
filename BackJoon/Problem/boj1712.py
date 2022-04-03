import math
A, B, C = map(int, input().split())

if B < C:
    print(math.floor(A/(C - B)) + 1)
else:
    print(-1)
