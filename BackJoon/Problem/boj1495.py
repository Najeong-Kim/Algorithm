import sys
input = sys.stdin.readline
from collections import deque

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
queue = deque()
queue.append([S, 0])
arr = [0] * (M + 1)
maxVolume = -1
while queue:
    [nowVolume, now] = queue.popleft()
    if now == N:
        maxVolume = max(maxVolume, nowVolume)
    else:
        upVolume, downVolume = nowVolume + V[now], nowVolume - V[now]
        thisTime = now + 1
        if upVolume <= M and [upVolume, thisTime] not in queue:
            queue.append([upVolume, thisTime])
        if downVolume >= 0 and [downVolume, thisTime] not in queue:
            queue.append([downVolume, thisTime])

print(max(maxVolume, -1))
