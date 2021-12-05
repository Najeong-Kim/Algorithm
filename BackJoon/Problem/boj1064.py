import sys
input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())

if xa == xb == xc or ya == yb == yc:
    print(-1)
elif xa-xb != 0 and xa-xc != 0 and (ya-yb)/(xa-xb) == (ya-yc)/(xa-xc):
    print(-1)
else:
    x = [xa, xb, xc]
    y = [ya, yb, yc]
    result = []
    for i in range(3):
        now = (
            ((x[i % 3] - x[(i + 1) % 3]) ** 2 + (y[i % 3] - y[(i + 1) % 3]) ** 2) ** (1 / 2)
            + ((x[(i + 1) % 3] - x[(i + 2) % 3]) ** 2 + (y[(i + 1) % 3] - y[(i + 2) % 3]) ** 2) ** (1 / 2)
        ) * 2
        result.append(now)
    print(max(result)-min(result))
