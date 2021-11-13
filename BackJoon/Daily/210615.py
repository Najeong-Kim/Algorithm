# 1992 쿼드트리

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# arr = []
# for i in range(N):
#     arr2 = list(map(int, input().rstrip()))
#     arr.append(arr2)
#
#
# def quad_tree(array, n):
#     standard = array[0][0]
#     check = 0
#     for a in range(n):
#         for b in range(n):
#             if array[a][b] != standard:
#                 check = 1
#             if check:
#                 break
#         if check:
#             break
#     if not check:
#         print(standard, end='')
#     if check:
#         print('(', end='')
#         quad_tree([row[0:n // 2] for row in array[0:n // 2]], n // 2)
#         quad_tree([row[n // 2:n] for row in array[0:n // 2]], n // 2)
#         quad_tree([row[0:n // 2] for row in array[n // 2:n]], n // 2)
#         quad_tree([row[n // 2:n] for row in array[n // 2:n]], n // 2)
#         print(')', end='')
#
#
# quad_tree(arr, N)


# 2579 계단 오르기

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# stair = [0] * (n+1)
# arr = [0] * (n+1)
#
# for i in range(1, n + 1):
#     stair[i] = int(input())
#
# for i in range(1, n + 1):
#     if i == 1:
#         arr[i] = stair[i]
#     elif i == 2:
#         arr[i] = arr[i - 1] + stair[i]
#     else:
#         arr[i] = max(arr[i - 2] + stair[i], arr[i - 3] + stair[i - 1] + stair[i])
#
# print(arr[n])


# 16928 뱀과 사다리 게임

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr_start = []
# arr_end = []
# queue = deque()
# queue.append(1)
# visited = [100] * 101
# visited[1] = 0
#
# for i in range(n + m):
#     a, b = map(int, input().split())
#     arr_start.append(a)
#     arr_end.append(b)
#
# while queue:
#     a = queue.popleft()
#     for i in range(1, 7):
#         if a + i <= 100 and visited[a + i] == 100:
#             visited[a + i] = visited[a] + 1
#             if (a + i) in arr_start:
#                 k = arr_end[arr_start.index(a + i)]
#                 visited[k] = min(visited[k], visited[a] + 1)
#                 queue.append(k)
#             else:
#                 queue.append(a + i)
#
# print(visited[100])


# 1107 리모컨

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# M = int(input())
# arr = list(map(int, input().split()))
# small = N
# big = N
# count = 0
# count2 = abs(N - 100)
# first_check = 0
#
# for i in arr:
#     if str(i) not in str(N):
#         first_check += 1
# if first_check == len(arr):
#     print(min(len(str(N)), count2))
#     exit()
# if M == 10:
#     print(count2)
#     exit()
# if M == 9 and 0 not in arr:
#     print(min(N+1, count2))
#     exit()
# if M == 0:
#     print(min(len(str(N)), count2))
#     exit()
#
# while True:
#     count += 1
#     if small > 0:
#         small -= 1
#     big += 1
#     check = 0
#     small_check = 0
#     big_check = 0
#     for i in arr:
#         if str(i) not in str(small):
#             small_check += 1
#     for i in arr:
#         if str(i) not in str(big):
#             big_check += 1
#     if small_check == len(arr):
#         count += len(str(small))
#         break
#     elif big_check == len(arr):
#         count += len(str(big))
#         break
#
# print(min(count, count2))


# 9019 DSLR

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# T = int(input())
# controls = ['D', 'S', 'L', 'R']
#
# for i in range(T):
#     A, B = map(int, input().split())
#     visited = [''] * 10000
#     visited[A] = ' '
#     queue = deque([A])
#     while queue:
#         n = queue.popleft()
#         for j in controls:
#             if j == 'D':
#                 if n * 2 <= 9999 and visited[n * 2] == '':
#                     visited[n * 2] = visited[n] + 'D'
#                     queue.append(n * 2)
#                 elif n * 2 > 9999 and visited[(n * 2) % 10000] == '':
#                     visited[(n * 2) % 10000] = visited[n] + 'D'
#                     queue.append((n * 2) % 10000)
#             elif j == 'S':
#                 if n != 0 and visited[n - 1] == '':
#                     visited[n - 1] = visited[n] + 'S'
#                     queue.append(n - 1)
#                 elif n == 0 and visited[9999] == '':
#                     visited[9999] = visited[n] + 'S'
#                     queue.append(9999)
#             elif j == 'L':
#                 array = list(map(int, str(n)))
#                 while len(array) != 4:
#                     array.insert(0, 0)
#                 number = array[0] + array[1] * 1000 + array[2] * 100 + array[3] * 10
#                 if visited[number] == '':
#                     visited[number] = visited[n] + 'L'
#                     queue.append(number)
#             elif j == 'R':
#                 array = list(map(int, str(n)))
#                 while len(array) != 4:
#                     array.insert(0, 0)
#                 number = array[0] * 100 + array[1] * 10 + array[2] + array[3] * 1000
#                 if visited[number] == '':
#                     visited[number] = visited[n] + 'R'
#                     queue.append(number)
#
#         if visited[B] != '':
#             break
#
#     print(visited[B][1:])


# 14500 테트로미노

# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
#
# check = [
#     [[0, 0], [0, 1], [0, 2], [0, 3]],
#     [[0, 0], [1, 0], [2, 0], [3, 0]],
#     [[0, 0], [1, 0], [2, 0], [2, 1]],
#     [[0, 1], [1, 1], [2, 1], [2, 0]],
#     [[0, 0], [1, 0], [1, 1], [1, 2]],
#     [[0, 2], [1, 2], [1, 1], [1, 0]],
#     [[1, 0], [0, 0], [0, 1], [0, 2]],
#     [[1, 2], [0, 0], [0, 1], [0, 2]],
#     [[2, 0], [1, 0], [0, 0], [0, 1]],
#     [[2, 1], [1, 1], [0, 1], [0, 0]],
#     [[0, 0], [1, 0], [1, 1], [2, 1]],
#     [[0, 1], [1, 1], [1, 0], [2, 0]],
#     [[0, 0], [0, 1], [1, 1], [1, 2]],
#     [[1, 0], [1, 1], [0, 1], [0, 2]],
#     [[0, 0], [0, 1], [0, 2], [1, 1]],
#     [[1, 0], [1, 1], [1, 2], [0, 1]],
#     [[0, 0], [1, 0], [2, 0], [1, 1]],
#     [[0, 1], [1, 1], [2, 1], [1, 0]],
#     [[0, 0], [0, 1], [1, 0], [1, 1]]
# ]
#
# result = 0
#
# for i in range(N):
#     for j in range(M):
#         for k in range(len(check)):
#             count = 0
#             for a in range(4):
#                 try:
#                     count += arr[i + check[k][a][0]][j + check[k][a][1]]
#                 except:
#                     count = -1
#                     break
#             if count == -1:
#                 continue
#             result = max(result, count)
#
# print(result)


# 16236 아기 상어

# import sys
# from collections import deque
# import heapq
#
# input = sys.stdin.readline
#
# N = int(input())
#
# arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
#
# x = 0
# y = 0
# size = 2
# count = 0
# time = 0
# fish = []
# now = []
# visited = []
# check = []
# queue = deque()
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 9:
#             x = i
#             y = j
#             arr[i][j] = 0
#         elif arr[i][j] != 0:
#             heapq.heappush(fish, (arr[i][j], i, j))
#
# if len(fish) == 0:
#     print(0)
#     exit()
#
#
# def initialize(a, b):
#     global visited
#     global queue
#     global check
#     queue = deque()
#     queue.append([a, b])
#     visited = [[-1] * N for _ in range(N)]
#     visited[a][b] = 0
#     check = []
#
#
# def find_fish():
#     while fish:
#         if fish[0][0] < size:
#             now.append(heapq.heappop(fish))
#         else:
#             break
#
#
# def find():
#     global count
#     global size
#     global visited
#     global time
#     global now
#     global queue
#     global check
#     while queue:
#         if len(now) == 0:
#             break
#         for _ in range(len(queue)):
#             x, y = queue.popleft()
#             for a in range(4):
#                 nx = x + dx[a]
#                 ny = y + dy[a]
#                 if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                     continue
#                 if visited[nx][ny] == -1 and arr[nx][ny] <= size:
#                     visited[nx][ny] = visited[x][y] + 1
#                     queue.append([nx, ny])
#                     for a in now:
#                         if a[1] == nx and a[2] == ny:
#                             check.append(a)
#         if check:
#             check.sort(key=lambda z: (z[1], z[2]))
#             x = check[0][1]
#             y = check[0][2]
#             count += 1
#             time += visited[x][y]
#             arr[x][y] = 0
#             now.remove(check[0])
#             initialize(x, y)
#             if count == size:
#                 size += 1
#                 count = 0
#                 find_fish()
#
# initialize(x, y)
# find_fish()
# find()
# print(time)
