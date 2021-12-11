import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
connect = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
parents[1] = 1
queue = deque()

for i in range(N - 1):
    x, y = map(int, input().split())
    connect[x].append(y)
    connect[y].append(x)

for i in connect[1]:
    queue.append([i, 1])

while queue:
    now, parent = queue.popleft()
    parents[now] = parent
    for i in connect[now]:
        if not parents[i]:
            queue.append([i, now])

for i in range(2, N+1):
    print(parents[i])
