# 1927 최소 힙

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n = int(input())
# heap = []
#
# for i in range(n):
#     a = int(input())
#     if a == 0 and len(heap) == 0:
#         print(0)
#     elif a == 0:
#         print(heapq.heappop(heap))
#     else:
#         heapq.heappush(heap, a)


# 7576 토마토

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# m, n = map(int, input().split())
#
# arr = []
#
# for _ in range(n):
#     arr2 = list(map(int, input().split()))
#     arr.append(arr2)
#
# queue = deque()
#
# visited = []
#
# time = [-1, 1, -1, 1]
# result = 0
#
# for _ in range(n):
#     visited2 = [False] * m
#     visited.append(visited2)
#
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1:
#             visited[i][j] = True
#             queue.append([i, j])
#
# while queue:
#     count = len(queue)
#     result += 1
#     for i in range(count):
#         c = queue.popleft()
#         if c[0] - 1 >= 0 and arr[c[0] - 1][c[1]] == 0:
#             arr[c[0] - 1][c[1]] = 1
#             queue.append([c[0] - 1, c[1]])
#             visited[c[0] - 1][c[1]] = True
#         if c[0] + 1 < n and arr[c[0] + 1][c[1]] == 0:
#             arr[c[0] + 1][c[1]] = 1
#             queue.append([c[0] + 1, c[1]])
#             visited[c[0] + 1][c[1]] = True
#         if c[1] - 1 >= 0 and arr[c[0]][c[1] - 1] == 0:
#             arr[c[0]][c[1] - 1] = 1
#             queue.append([c[0], c[1] - 1])
#             visited[c[0]][c[1] - 1] = True
#         if c[1] + 1 < m and arr[c[0]][c[1] + 1] == 0:
#             arr[c[0]][c[1] + 1] = 1
#             queue.append([c[0], c[1] + 1])
#             visited[c[0]][c[1] + 1] = True
#
# check = 0
# stop = False
#
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 0:
#             print(-1)
#             stop = True
#             if stop:
#                 break
#         else:
#             check += 1
#     if stop:
#         break
#
# if check == n * m:
#     if result == 0:
#         print(0)
#     else:
#         print(result - 1)


# 11279 최대 힙

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# heap = []
#
# n = int(input())
#
# for i in range(n):
#     a = int(input())
#     if a == 0 and len(heap) == 0:
#         print(0)
#     elif a == 0:
#         print(heapq.heappop(heap) * -1)
#     else:
#         heapq.heappush(heap, a * -1)


# 11047 동전 0

# import sys
#
# input = sys.stdin.readline
# coin = []
# count = 0
#
# n, k = map(int, input().split())
#
# for i in range(n):
#     coin.append(int(input()))
#
# for i in range(1, n + 1):
#     if k // coin[-i] != 0:
#         count += (k // coin[-i])
#         k = k % coin[-i]
#
# print(count)


# 9095 1, 2, 3 더하기

# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# arr = [-1] * 11
# arr[0] = 0
# arr[1] = 1
# arr[2] = 2
# arr[3] = 4
#
# for i in range(T):
#     a = int(input())
#     for j in range(a+1):
#         if arr[j] == -1:
#             arr[j] = arr[j-1] + arr[j-2] + arr[j-3]
#     print(arr[a])


# 1389 케빈 베이컨의 6단계 법칙

# import sys
#
# input = sys.stdin.readline
#
# INF = int(1e9)
#
# n, m = map(int, input().split())
#
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
#
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
#
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# number = 1e9
# index = 0
#
# for a in range(1, n + 1):
#     if sum(graph[a][1:n + 1]) < number:
#         number = sum(graph[a][1:n + 1])
#         index = a
#
# print(index)


# 2667 단지번호붙이기

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().rstrip())))
#
# arr = [0] * 26*26
#
#
# def dfs(x, y, number):
#     if x <= -1 or x >= n or y <= -1 or y >= n:
#         return False
#     if graph[x][y] == 1:
#         arr[number] += 1
#         graph[x][y] = 0
#         dfs(x - 1, y, number)
#         dfs(x, y - 1, number)
#         dfs(x + 1, y, number)
#         dfs(x, y + 1, number)
#         return True
#     return False
#
#
# result = 0
#
# for i in range(n):
#     for j in range(n):
#         if dfs(i, j, result):
#             result += 1
#
# print(result)
# arr.sort()
# for i in arr:
#     if i != 0:
#         print(i)


# 17219 비밀번호 찾기

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# dic = {}
#
# for i in range(n):
#     a, b = map(str, input().split())
#     dic[a] = b
#
# for i in range(m):
#     print(dic[input().rstrip()])


# 11403 경로 찾기

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr2 = list(map(int, input().rstrip().split()))
#     arr.append(arr2)
#
# for k in range(n):
#     for a in range(n):
#         for b in range(n):
#             if arr[a][k] + arr[k][b] == 2:
#                 arr[a][b] = 1
#
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end=' ')
#     print('')


# 11399 ATM

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = list(map(int, input().rstrip().split()))
#
# heap = []
#
# for i in arr:
#     heapq.heappush(heap, i)
#
# total = 0
# count = 0
#
# while heap:
#     count += heapq.heappop(heap)
#     total += count
#
# print(total)
