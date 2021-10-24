# 1543 문서 검색

# doc = input().rstrip()
# word = input().rstrip()
# count = 0
# check = -1
#
# for i in range(len(doc) - len(word) + 1):
#     if doc[i:i+len(word)] == word:
#         if check < i:
#             count += 1
#             check = i+len(word)-1
#
# print(count)


# 1568 새

# N = int(input())
# count = 0
# check = 1
#
# while N:
#     if N >= check:
#         count += 1
#         N -= check
#         check += 1
#     else:
#         check = 1
#
# print(count)


# 1302 베스트셀러

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# books = {}
#
# for i in range(N):
#     book = input().rstrip()
#     if book in books:
#         books[book] += 1
#     else:
#         books[book] = 1
#
# best = max(books.values())
# result = []
#
# for i in books.keys():
#     if books[i] == best:
#         result.append(i)
#
# result.sort()
#
# print(result[0])


# 1668 트로피 진열

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = []
# left = 0
# left_check = 0
# right = 0
# right_check = 0
#
# for i in range(N):
#     arr.append(int(input()))
#
# for i in range(len(arr)):
#     if arr[i] > left_check:
#         left += 1
#         left_check = arr[i]
#     if arr[-1 - i] > right_check:
#         right += 1
#         right_check = arr[-1 - i]
#
# print(left)
# print(right)


# 1236 성 지키기

# N, M = map(int, input().split())
#
# arr = []
#
# for i in range(N):
#     line = input().rstrip()
#     arr2 = []
#     for j in range(len(line)):
#         arr2.append(line[j])
#     arr.append(arr2)
#
# x = 0
# y = M
#
# for i in range(N):
#     if 'X' not in arr[i]:
#         x += 1
#
# for i in range(M):
#     for j in range(N):
#         if arr[j][i] == 'X':
#             y -= 1
#             break
#
# print(max(x, y))


# 11004 K번째 수

# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
#
# arr = list(map(int, input().split()))
# arr.sort()
#
# print(arr[K - 1])
