# 9037 The candy war

# import sys
# input = sys.stdin.readline
#
# T = int(input())
#
# for i in range(T):
#     N = int(input())
#     C = list(map(int, input().split()))
#     result = 0
#     for j in range(len(C)):
#         if C[j] % 2 == 1:
#             C[j] += 1
#     standard = C[0]
#     finish = False
#     for j in range(len(C)):
#         if C[j] != standard:
#             finish = True
#     while finish:
#         result += 1
#         count = 0
#         now = []
#         for j in range(len(C)):
#             plus = 0
#             if j < len(C) - 1:
#                 plus = j + 1
#             now.append(C[j] // 2 + C[plus] // 2)
#         for j in range(len(now)):
#             if now[j] % 2 == 1:
#                 now[j] += 1
#         standard = now[0]
#         for j in range(len(now)):
#             if now[j] != standard:
#                 count += 1
#         if count == 0:
#             break
#         else:
#             C = now
#     print(result)


# 16769 Mixing Milk

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))
# check = [A, B, C]
# first = 0
# second = 1
#
# for i in range(100):
#     if first == 2:
#         second = 0
#     else:
#         second = first + 1
#     if check[second][0] - check[second][1] >= check[first][1]:
#         check[second][1] += check[first][1]
#         check[first][1] = 0
#     else:
#         check[first][1] -= check[second][0] - check[second][1]
#         check[second][1] = check[second][0]
#     if first == 2:
#         first = 0
#     else:
#         first += 1
#
# print(A[1])
# print(B[1])
# print(C[1])


# 17224 APC는 왜 서브태스크 대회가 되었을까?

# import sys
# input = sys.stdin.readline
#
# N, L, K = map(int, input().split())
# tasks = []
#
# for i in range(N):
#     sub1, sub2 = map(int, input().split())
#     tasks.append([sub1, sub2])
#
# sortTasks = sorted(tasks, key=lambda x: (x[1], x[0]))
#
# score = 0
# check = 0
#
# for i in range(len(sortTasks)):
#     if K == 0:
#         break
#     if sortTasks[i][1] <= L:
#         score += 140
#         check += 1
#     elif sortTasks[i][0] <= L:
#         score += 100
#         check += 1
#     if check == K:
#         break
#
# print(score)


# 2480 주사위 세개

# A, B, C = map(int, input().split())
#
# if A == B == C:
#     print(10000 + A * 1000)
# elif A == B and B != C:
#     print(1000 + A * 100)
# elif B == C and A != B:
#     print(1000 + B * 100)
# elif C == A and A != B:
#     print(1000 + A * 100)
# elif A != B and B != C:
#     print(max(A, B, C) * 100)


# 17413 단어 뒤집기 2

# N = input().rstrip()
#
# openTag = False
# check = []
# result = ''
#
# for i in range(len(N)):
#     if N[i] == '<':
#         check.reverse()
#         result += ''.join(check)
#         check = []
#         openTag = True
#         result += N[i]
#     elif N[i] == '>':
#         openTag = False
#         result += N[i]
#     else:
#         if openTag is True:
#             result += N[i]
#         else:
#             if N[i] == ' ':
#                 check.reverse()
#                 result += ''.join(check)
#                 result += ' '
#                 check = []
#             else:
#                 check.append(N[i])
#
# check.reverse()
# result += ''.join(check)
# check = []
#
# print(result)
