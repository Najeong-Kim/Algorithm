# 14502 연구소

# import sys
# from collections import deque
# from itertools import combinations
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = []
# queue = deque()
#
# for i in range(N):
#     arr2 = list(map(int, input().rstrip().split()))
#     arr.append(arr2)
#
#
# def initialize():
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 2:
#                 queue.append([i, j])
#
#
# empty = []
# wall_count = 0
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             empty.append([i, j])
#         if arr[i][j] == 1:
#             wall_count += 1
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(queue):
#     visited = [[False] * M for _ in range(N)]
#     for i in queue:
#         visited[i[0]][i[1]] = True
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             else:
#                 if not visited[nx][ny] and arr[nx][ny] == 0:
#                     queue.append([nx, ny])
#                     visited[nx][ny] = True
#     return visited
#
#
# wall = list(combinations(empty, 3))
#
# maxCount = 0
#
# for i in wall:
#     for j in i:
#         arr[j[0]][j[1]] = 1
#     initialize()
#     visited = bfs(queue)
#     count = 0
#     for a in range(N):
#         for b in range(M):
#             if not visited[a][b]:
#                 count += 1
#     maxCount = max(count - (wall_count + 3), maxCount)
#     for j in i:
#         arr[j[0]][j[1]] = 0
#
# print(maxCount)


# 1991 트리 순회

# import sys
# input = sys.stdin.readline
#
#
# def pre_order(node):
#     if tree[node]:
#         print(node, end='')
#         if tree[node][0] != '.':
#             pre_order(tree[node][0])
#         if tree[node][1] != '.':
#             pre_order(tree[node][1])
#
#
# def mid_order(node):
#     if tree[node]:
#         if tree[node][0] != '.':
#             mid_order(tree[node][0])
#         print(node, end='')
#         if tree[node][1] != '.':
#             mid_order(tree[node][1])
#
#
# def post_order(node):
#     if tree[node]:
#         if tree[node][0] != '.':
#             post_order(tree[node][0])
#         if tree[node][1] != '.':
#             post_order(tree[node][1])
#         print(node, end='')
#
#
# N = int(input())
# tree = {}
#
# for i in range(N):
#     a, b, c = map(str, input().rstrip().split())
#     tree[a] = [b, c]
#
# pre_order('A')
# print('')
# mid_order('A')
# print('')
# post_order('A')


# 14938 서강그라운드

# import sys
# input = sys.stdin.readline
#
# INF = int(1e9)
# n, m, r = map(int, input().rstrip().split())
#
# items = list(map(int, input().rstrip().split()))
# field = [[INF] * (n + 1) for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     field[i][i] = 0
#
# for i in range(r):
#     a, b, c = map(int, input().split())
#     if field[a][b] > c:
#         field[a][b] = c
#         field[b][a] = c
#
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             field[i][j] = min(field[i][j], field[i][k] + field[k][j])
#
# maxItem = 0
#
# for i in range(1, n + 1):
#     count = 0
#     for j in range(len(field[i])):
#         if field[i][j] <= m:
#             count += items[j - 1]
#     maxItem = max(count, maxItem)
#
# print(maxItem)


# 11404 플로이드

# import sys
# input = sys.stdin.readline
#
# INF = int(1e9)
# n = int(input())
# m = int(input())
#
# roads = [[INF] * (n + 1) for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     roads[i][i] = 0
#
# for i in range(m):
#     a, b, c = map(int, input().split())
#     if roads[a][b] > c:
#         roads[a][b] = c
#
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             roads[i][j] = min(roads[i][j], roads[i][k] + roads[k][j])
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if roads[i][j] != INF:
#             print(roads[i][j], end=' ')
#         else:
#             print(0, end=' ')
#     print('')


# 1753 최단경로

# import sys
# import heapq
# input = sys.stdin.readline
#
# INF = int(1e9)
# V, E = map(int, input().split())
# K = int(input())
# arr = [[] for _ in range(V + 1)]
# distance = [INF] * (V + 1)
#
# for i in range(E):
#     u, v, w = map(int, input().split())
#     arr[u].append((v, w))
#
# print(arr)
#
# def dijkstra(start):
#     queue = []
#     heapq.heappush(queue, (0, start))
#     distance[start] = 0
#     while queue:
#         dist, now = heapq.heappop(queue)
#         print(dist, now)
#         if distance[now] < dist:
#             continue
#         for i in arr[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(queue, (cost, i[0]))
#
#
# dijkstra(K)
#
# for i in range(1, V + 1):
#     if distance[i] == INF:
#         print('INF')
#     else:
#         print(distance[i])


# 1149 RGB거리

# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# A = 0
# B = 0
# C = 0
# result = [0] * 3
#
# for i in range(N):
#     a, b, c = map(int, input().split())
#     if i == 0:
#         A = a
#         B = b
#         C = c
#     else:
#         result[0] = min(B, C) + a
#         result[1] = min(A, C) + b
#         result[2] = min(A, B) + c
#         A, B, C = result[0], result[1], result[2]
#
# print(min(A, B, C))
