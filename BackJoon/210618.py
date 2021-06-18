# 11660 구간 합 구하기 5

# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = []
#
# for i in range(N):
#     arr2 = list(map(int, input().rstrip().split()))
#     arr3 = []
#     count = 0
#     for j in range(len(arr2)):
#         if len(arr) == 0:
#             count += arr2[j]
#             arr3.append(count)
#         else:
#             count += arr2[j]
#             arr3.append(count + arr[len(arr)-1][j])
#     arr.append(arr3)
#
# for i in range(M):
#     x1, y1, x2, y2 = map(int, input().rstrip().split())
#     x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
#     if x1 == 0 and y1 == 0:
#         total = arr[x2][y2]
#     elif x1 == 0:
#         total = arr[x2][y2] - arr[x2][y1-1]
#     elif y1 == 0:
#         total = arr[x2][y2] - arr[x1 - 1][y2]
#     else:
#         total = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
#     print(total)


# 2407 조합

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().rstrip().split())
#
# a = 1
# b = 1
#
# for i in range(m):
#     a *= n-i
#     b *= (i+1)
#
# print(int(a//b))


# 16953 A → B

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# A, B = map(int, input().rstrip().split())
#
# queue = deque()
# queue.append(A)
#
# visited = {}
# visited[A] = 1
#
# while queue:
#     x = queue.popleft()
#     if x*2 <= B and x*2 not in visited:
#         queue.append(x*2)
#         visited[x*2] = visited[x] + 1
#     if (x*10 + 1) <= B and (x*10 + 1) not in visited:
#         queue.append(x*10 + 1)
#         visited[x*10 + 1] = visited[x] + 1
#
# if B in visited:
#     print(visited[B])
# else:
#     print(-1)
