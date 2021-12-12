import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
INF = int(100000000)

graph = [[] for _ in range(N + 1)]
costs = [INF] * (N + 1)

for i in range(M):
    inputStart, inputEnd, inputCost = map(int, input().split())
    check = 0
    for i in range(len(graph[inputStart])):
        if graph[inputStart][i][0] == inputEnd:
            check = 1
            if graph[inputStart][i][1] > inputCost:
                graph[inputStart][i][1] = inputCost
    if check == 0:
        graph[inputStart].append([inputEnd, inputCost])

start, end = map(int, input().split())

heap = []
heapq.heappush(heap, (0, start))

while heap:
    now = heapq.heappop(heap)
    nowCost = now[0]
    nowStart = now[1]
    for i in range(len(graph[nowStart])):
        nowEnd = graph[nowStart][i][0]
        addCost = graph[nowStart][i][1]
        if costs[nowEnd] > nowCost + addCost:
            costs[nowEnd] = nowCost + addCost
            heapq.heappush(heap, (costs[nowEnd], nowEnd))

print(costs[end])
