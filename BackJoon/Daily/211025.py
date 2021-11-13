# 2012 등수 매기기

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = []
# result = 0
#
# for i in range(N):
#     arr.append(int(input()))
#
# arr.sort()
#
# for i in range(len(arr)):
#     result += abs(arr[i] - (i+1))
#
# print(result)


# 1325 효율적인 해킹

# import sys
# from collections import deque
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# check = {}
# result = [0] * 10001
#
# for i in range(M):
#     one, two = map(int, input().split())
#     if two in check:
#         check[two].append(one)
#     else:
#         check[two] = [one]
#
# for i in range(1, N + 1):
#     if i in check:
#         queue = deque()
#         now = 1
#         hacking = [False] * (N + 1)
#         hacking[i] = True
#         queue.append(i)
#         while queue:
#             k = queue.popleft()
#             if k in check:
#                 for j in check[k]:
#                     if hacking[j] is False:
#                         queue.append(j)
#                         hacking[j] = True
#                         now += 1
#         result[i] = now
#
# answer = []
# maxNum = max(result)
#
# for i in range(len(result)):
#     if maxNum == result[i]:
#         answer.append(str(i))
#
# print(' '.join(answer))
