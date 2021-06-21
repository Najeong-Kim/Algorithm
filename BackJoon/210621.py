# 1916 최소비용 구하기

# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# N = int(input())
# M = int(input())
#
# graph = [[] for i in range(N + 1)]
# visited = [False] * (N + 1)
# distance = [INF] * (N + 1)
#
# for _ in range(M):
#     a, b, c = map(int, input().rstrip().split())
#     check = 0
#     if len(graph[a]) != 0:
#         for i in graph[a]:
#             if i[0] == b and i[1] < c:
#                 check = 1
#     if check == 0:
#         graph[a].append([b, c])
#
# x, y = map(int, input().rstrip().split())
#
#
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, N + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index
#
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(N - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#
#
# dijkstra(x)
#
# print(distance[y])


# 2096 내려가기

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# max_arr = [0] * 3
# result = [0] * 3
# min_arr = [0] * 3
#
# a, b, c = map(int, input().split())
# max_arr[0], max_arr[1], max_arr[2] = a, b, c
# min_arr[0], min_arr[1], min_arr[2] = a, b, c
#
# for i in range(1, N):
#     a, b, c = map(int, input().split())
#     result[0] = max(max_arr[0], max_arr[1]) + a
#     result[1] = max(max_arr[0], max_arr[1], max_arr[2]) + b
#     result[2] = max(max_arr[1], max_arr[2]) + c
#     for j in range(len(result)):
#         max_arr[j] = result[j]
#         result[j] = 0
#     result[0] = min(min_arr[0], min_arr[1]) + a
#     result[1] = min(min_arr[0], min_arr[1], min_arr[2]) + b
#     result[2] = min(min_arr[1], min_arr[2]) + c
#     for j in range(len(result)):
#         min_arr[j] = result[j]
#         result[j] = 0
#
# print(max(max_arr), min(min_arr))


# 1932 정수 삼각형

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# k = int(input())
# arr = [0] * n
# result = [0] * n
# arr[0] = k
#
# for i in range(1, n):
#     line = list(map(int, input().rstrip().split()))
#     for j in range(len(line)):
#         if j == 0:
#             result[j] = arr[j] + line[j]
#         elif j == len(line) - 1:
#             result[j] = arr[j - 1] + line[j]
#         else:
#             result[j] = max(arr[j - 1], arr[j]) + line[j]
#     for j in range(len(result)):
#         arr[j] = result[j]
#         result[j] = 0
#
# print(max(arr))
