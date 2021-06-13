# 1074 Z

# import sys
#
# input = sys.stdin.readline
#
# N, r, c = map(int, input().split())
#
# count = 0
#
#
# def z(N, r, c):
#     global count
#     if N == 1:
#         if r == 0 and c == 0:
#             count += 0
#         elif r == 0 and c == 1:
#             count += 1
#         elif r == 1 and c == 0:
#             count += 2
#         elif r == 1 and c == 1:
#             count += 3
#     else:
#         if r // (2**(N-1)) == 0 and c // (2**(N-1)) == 0:
#             count += 0
#         if r // (2**(N-1)) == 0 and c // (2**(N-1)) == 1:
#             count += 4**(N-1)
#         if r // (2**(N-1)) == 1 and c // (2**(N-1)) == 0:
#             count += (4**(N-1))*2
#         if r // (2**(N-1)) == 1 and c // (2**(N-1)) == 1:
#             count += (4**(N-1))*3
#         z(N-1, r % (2**(N-1)), c % (2**(N-1)))
#
#
# z(N, r, c)
#
# print(count)


# 1620 나는야 포켓몬 마스터 이다솜

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# dic = {}
# dic2 = {}
# count = 1
#
# for _ in range(n):
#     i = input().rstrip()
#     dic[count] = i
#     dic2[i] = count
#     count += 1
#
# for _ in range(m):
#     i = input().rstrip()
#     try:
#         i = int(i)
#     except:
#         i = str(i)
#     if type(i) is int:
#         print(dic.get(i))
#     if type(i) is str:
#         print(dic2.get(i))


# 11286 절댓값 힙

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
#         k = heapq.heappop(heap)
#         print(k[1])
#     else:
#         heapq.heappush(heap, (abs(a), a))


# 7569 토마토

# import sys
# from collections import deque
#
# m, n, h = map(int, input().split())
#
# arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
#
# queue = deque()
#
# for i in range(m):
#     for j in range(n):
#         for k in range(h):
#             if arr[k][j][i] == 1:
#                 queue.append([i, j, k])
#
# day = 0
#
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [0, 0, 0, 0, -1, 1]
#
# while queue:
#     day += 1
#     for i in range(len(queue)):
#         x, y, z = queue.popleft()
#         for j in range(6):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             nz = z + dz[j]
#             if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h:
#                 continue
#             if arr[nz][ny][nx] == 0:
#                 arr[nz][ny][nx] = 1
#                 queue.append([nx, ny, nz])
#
# for i in range(m):
#     for j in range(n):
#         for k in range(h):
#             if arr[k][j][i] == 0:
#                 print(-1)
#                 exit()
#
# print(day - 1)


# 6064 카잉 달력

# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for i in range(T):
#     day = 0
#     count = 0
#     M, N, x, y = map(int, input().split())
#     while day == 0:
#         if ((M * count) + x) % N == y % N:
#             day = M * count + x
#             break
#         count += 1
#         if count > N:
#             day = -1
#     print(day)


# 9375 패션왕 신해빈

# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for i in range(T):
#     n = int(input())
#     dic = {}
#     for j in range(n):
#         a, b = map(str, input().split())
#         if b not in dic:
#             dic[b] = 0
#         dic[b] += 1
#     result = 1
#
#     for j in range(len(dic.values())):
#         result *= (list(dic.values())[j] + 1)
#
#     print(result - 1)


# 11726 2×n 타일링

# n = int(input())
#
# arr = [0] * 1001
# arr[1] = 1
# arr[2] = 2
#
# for i in range(3, n + 1):
#     arr[i] = arr[i - 1] + arr[i - 2]
#
# print(arr[n] % 10007)


# 18870 좌표 압축

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# N = int(input())
#
# heap = []
#
# arr = list(map(int, input().split()))
# arr2 = [0] * N
#
# for i in range(len(arr)):
#     heapq.heappush(heap, (arr[i], i))
#
# count = 0
# b = 2e9
# c = 2e9
# for i in arr:
#     a = heapq.heappop(heap)
#     if arr[a[1]] == b:
#         arr2[a[1]] = arr2[c]
#     else:
#         arr2[a[1]] = count
#         count += 1
#
#     b = arr[a[1]]
#     c = a[1]
#
# for i in arr2:
#     print(i, end=' ')


# 2606 바이러스

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
#
# arr = [[] for _ in range(n + 1)]
# queue = deque()
# visited = [False] * (n + 1)
#
# for i in range(m):
#     a, b = map(int, input().split())
#     arr[a].append(b)
#     arr[b].append(a)
#
# for i in arr[1]:
#     queue.append(i)
# visited[1] = True
# count = 0
#
# while queue:
#     k = queue.popleft()
#     if not visited[k]:
#         visited[k] = True
#         count += 1
#         if len(arr[k]) > 0:
#             for i in arr[k]:
#                 queue.append(i)
#
# print(count)


# 1931 회의실 배정

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n = int(input())
# heap = []
#
# for i in range(n):
#     a, b = map(int, input().split())
#     heapq.heappush(heap, (b, a))
#
# result = 0
# pre = -1
#
# while heap:
#     k = heapq.heappop(heap)
#     print(k)
#     if k[1] >= pre:
#         result += 1
#         pre = k[0]
#
# print(result)


# 9461 파도반 수열

# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# arr = [0] * 101
# arr[1] = 1
# arr[2] = 1
# arr[3] = 1
# arr[4] = 2
#
# for i in range(T):
#     N = int(input())
#
#     for j in range(5, N + 1):
#         arr[j] = arr[j - 1] + arr[j - 5]
#
#     print(arr[N])


# 11727 2×n 타일링 2

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = [0] * 1001
# arr[1] = 1
# arr[2] = 3
#
# for i in range(3, n + 1):
#     arr[i] = arr[i - 1] + arr[i - 2] * 2
#
# print(arr[n] % 10007)
