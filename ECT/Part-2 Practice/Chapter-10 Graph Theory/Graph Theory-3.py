from collections import deque

n = int(input())

data = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)

graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    data[i] = list(map(int, input().split()))
    for j in range(1, len(data[i])):
        if data[i][j] != -1:
            graph[data[i][j]].append(i)
            indegree[i] += 1


def topology_sort():
    count = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        count[i] = data[i][0]

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            count[i] = max(count[i], count[now] + data[i][0])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, len(count)):
        print(count[i])


topology_sort()
