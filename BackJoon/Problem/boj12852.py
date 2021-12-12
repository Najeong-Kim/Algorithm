import sys
input = sys.stdin.readline
from collections import deque
import copy

N = int(input())

arr = [[] for _ in range(N + 1)]
arr[N] = [N]
queue = deque()
queue.append(N)
while queue:
    now = queue.popleft()
    if now % 3 == 0:
        value = now // 3
        if len(arr[value]) == 0 or len(arr[value]) > (len(arr[now]) + 1):
            arr[value] = copy.deepcopy(arr[now])
            arr[value].append(value)
            queue.append(value)
            if value == 1:
                break
    if now % 2 == 0:
        value = now // 2
        if len(arr[value]) == 0 or len(arr[value]) > (len(arr[now]) + 1):
            arr[value] = copy.deepcopy(arr[now])
            arr[value].append(value)
            queue.append(value)
            if value == 1:
                break
    value = now - 1
    if len(arr[value]) == 0 or len(arr[value]) > (len(arr[now]) + 1):
        arr[value] = copy.deepcopy(arr[now])
        arr[value].append(value)
        queue.append(value)
        if value == 1:
            break

print(len(arr[1]) - 1)
for i in arr[1]:
    print(i, end=' ')
