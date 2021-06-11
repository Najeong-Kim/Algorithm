# 1018 체스판 다시 칠하기

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = []
# arr_first = []
# arr_second = []
# minNum = n * m
#
# for i in range(n):
#     a = input()
#     arr2 = []
#     arr3 = []
#     arr4 = []
#     for j in range(m):
#         arr2.append(a[j])
#         arr3.append(0)
#         arr4.append(0)
#     arr.append(arr2)
#     arr_first.append(arr3)
#     arr_second.append(arr4)
#
# for i in range(n):
#     for j in range(m):
#         if (i + j) % 2 == 0:
#             if arr[i][j] == 'B':
#                 arr_first[i][j] = 0
#                 arr_second[i][j] = 1
#             else:
#                 arr_first[i][j] = 1
#                 arr_second[i][j] = 0
#         if (i + j) % 2 == 1:
#             if arr[i][j] == 'W':
#                 arr_first[i][j] = 0
#                 arr_second[i][j] = 1
#             else:
#                 arr_first[i][j] = 1
#                 arr_second[i][j] = 0
#
# for i in range(n-7):
#     for j in range(m-7):
#         count = 0
#         count2 = 0
#         for k in range(8):
#             for l in range(8):
#                 count += arr_first[k+i][l+j]
#                 count2 += arr_second[k+i][l+j]
#         minNum = min(minNum, count, count2)
#
# print(minNum)


# 1654 랜선 자르기

# import sys
#
# input = sys.stdin.readline
#
# n, k = map(int, input().rstrip().split())
# arr = []
#
# for i in range(n):
#     arr.append(int(input()))
#
#
# def binary_search(array, target, start, end):
#     max_num = 0
#     while start <= end:
#         mid = (start + end) // 2
#         count = 0
#         for j in range(n):
#             count += array[j] // mid
#         if count >= target:
#             max_num = max(max_num, mid)
#             start = mid + 1
#         else:
#             end = mid - 1
#     return max_num
#
#
# print(binary_search(arr, k, 1, max(arr)))


# 2805 나무 자르기

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().rstrip().split())
# arr = list(map(int, input().rstrip().split()))
#
#
# def binary_search(array, target, start, end):
#     max_num = 0
#     while start <= end:
#         mid = (start + end) // 2
#         count = 0
#         for i in range(len(array)):
#             if array[i] >= mid:
#                 count += array[i] - mid
#         if count >= target:
#             max_num = max(mid, max_num)
#             start = mid + 1
#         else:
#             end = mid - 1
#     return max_num
#
#
# print(binary_search(arr, m, 0, max(arr)))


# 7568 덩치

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# arr2 = [0] * n
#
# for i in range(n):
#     a, b = map(int, input().rstrip().split())
#     arr.append([a, b])
#
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
#             count += 1
#     arr2[i] = count + 1
#
# for i in arr2:
#     print(i, end=' ')


# 18111 마인크래프트

# import sys
#
# input = sys.stdin.readline
#
# n, m, b = map(int, input().rstrip().split())
# arr = []
#
# for i in range(n):
#     arr2 = list(map(int, input().rstrip().split()))
#     arr.append(arr2)
#
# dic = {}
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] not in dic:
#             dic[arr[i][j]] = 1
#         else:
#             dic[arr[i][j]] += 1
#
# max_num = max(dic.keys())
# min_num = min(dic.keys())
#
# min_time = 10 ** 30
# max_height = 0
#
# for k in range(min_num, max_num+1):
#     time = 0
#     inventory = b
#     for i in dic:
#         if i < k:
#             inventory -= dic[i] * (k - i)
#             time += dic[i] * (k - i)
#         if i > k:
#             inventory += dic[i] * (i - k)
#             time += dic[i] * 2 * (i - k)
#     if inventory >= 0 and time <= min_time:
#         min_time = time
#         max_height = k
#
# print(min_time)
# print(max_height)


# 1003 피보나치 함수

# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for i in range(T):
#     N = int(input())
#     zero = 0
#     one = 0
#     arr = []
#     for _ in range(N+1):
#         arr.append([0, 0])
#     for j in range(N+1):
#         if j == 0:
#             arr[j] = [1, 0]
#         elif j == 1:
#             arr[j] = [0, 1]
#         else:
#             arr[j] = [arr[j-1][0] + arr[j-2][0], arr[j-1][1] + arr[j-2][1]]
#
#     print(arr[N][0], arr[N][1])


# 1012 유기농 배추

# import sys
# from collections import deque
#
# input = sys.stdin.readline
# queue = deque()
#
# T = int(input())
# for i in range(T):
#     m, n, k = map(int, input().split())
#     arr = []
#     count = 0
#
#     for _ in range(n):
#         arr.append([0] * m)
#
#     for _ in range(k):
#         x, y = map(int, input().split())
#         arr[y][x] = 1
#
#     for a in range(n):
#         for b in range(m):
#             if arr[a][b] == 1:
#                 count += 1
#                 arr[a][b] = 2
#                 queue.append([a, b])
#             while queue:
#                 c = queue.popleft()
#                 if c[0] >= 1 and arr[c[0] - 1][c[1]] == 1:
#                     arr[c[0] - 1][c[1]] = 2
#                     queue.append([c[0] - 1, c[1]])
#                 if c[0] < n - 1 and arr[c[0] + 1][c[1]] == 1:
#                     arr[c[0] + 1][c[1]] = 2
#                     queue.append([c[0] + 1, c[1]])
#                 if c[1] >= 1 and arr[c[0]][c[1] - 1] == 1:
#                     arr[c[0]][c[1] - 1] = 2
#                     queue.append([c[0], c[1] - 1])
#                 if c[1] < m - 1 and arr[c[0]][c[1] + 1] == 1:
#                     arr[c[0]][c[1] + 1] = 2
#                     queue.append([c[0], c[1] + 1])
#
#     print(count)


# 1463 1로 만들기

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = [1000000] * 1000001
# arr[0] = 0
# arr[1] = 0
#
# if n >= 2:
#     for i in range(2, n + 1):
#         if i % 3 == 0:
#             arr[i] = min(arr[i], arr[i//3] + 1)
#         if i % 2 == 0:
#             arr[i] = min(arr[i], arr[i//2] + 1)
#         arr[i] = min(arr[i], arr[i - 1] + 1)
#
# print(arr[n])
