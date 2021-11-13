# 15969 행복

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# print(max(arr) - min(arr))


# 10539 수빈이와 수열

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
# result = [0] * N
#
# for i in range(len(arr)):
#     result[i] = (arr[i]) * (i+1) - sum(result[0:i])
#
# for i in range(len(result)):
#     result[i] = str(result[i])
#
# print(' '.join(result))


# 17269 이름궁합 테스트

# N, M = map(int, input().split())
# A, B = map(str, input().split())
#
# times = {
#     'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1,
#     'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2,
#     'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1,
#     'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1
#     }
#
# init = []
# total = ''
# extra = ''
#
# if len(A) > len(B):
#     extra = A[len(B):]
# elif len(A) < len(B):
#     extra = B[len(A):]
#
# for i in range(min(len(A), len(B))):
#     total += A[i] + B[i]
#
# total += extra
#
# for i in range(len(total)):
#     init.append(times[total[i]])
#
#
# for i in range(len(init) - 2):
#     temp = []
#     for j in range(len(init) - 1):
#         temp.append((init[j] + init[j + 1]) % 10)
#     init = temp
#
# if init[0] == 0:
#     print(str(init[1]) + '%')
# else :
#     print(str(init[0]) + str(init[1]) + '%')


# 17389 보너스 점수

# N = int(input())
# score = input()
# total = 0
# bonus = 0
#
# for i in range(len(score)):
#     if score[i] == 'O':
#         total += i + 1 + bonus
#         bonus += 1
#     else:
#         bonus = 0
#
# print(total)


# 16165 걸그룹 마스터 준석이

# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# group = {}
#
# for i in range(N):
#     team = input().rstrip()
#     n = int(input())
#     group[team] = []
#     for j in range(n):
#         group[team].append(input().rstrip())
#     group[team].sort()
#
# for i in range(M):
#     text = input().rstrip()
#     type = int(input())
#     if type == 0:
#         print('\n'.join(group[text]))
#     else:
#         for team, members in group.items():
#             if text in members:
#                 print(team)
#                 break


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


# 16675 두 개의 손

# ML, MR, TL, TR = map(str, input().split())
#
# value = ['S', 'R', 'P']
#
# M = [ML, MR]
# T = [TL, TR]
#
# if 'S' in M and 'R' not in T and 'S' not in T:
#     print('MS')
# elif 'R' in M and 'P' not in T and 'R' not in T:
#     print('MS')
# elif 'P' in M and 'S' not in T and 'P' not in T:
#     print('MS')
# elif 'S' in T and 'R' not in M and 'S' not in M:
#     print('TK')
# elif 'R' in T and 'P' not in M and 'R' not in M:
#     print('TK')
# elif 'P' in T and 'S' not in M and 'P' not in M:
#     print('TK')
# else:
#     print('?')
