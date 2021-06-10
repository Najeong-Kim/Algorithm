# 1436 영화감독 숌

# import sys
#
# input = sys.stdin.readline
#
# n = int(input().split()[0])
# number = 0
# count = 0
#
# while True:
#     number += 1
#     if '666' in str(number):
#         count += 1
#     if count == n:
#         print(number)
#         break


# 1929 소수 구하기

# import sys
#
# input = sys.stdin.readline
#
# x, y = map(int, input().rstrip().split())
#
# def prime_list(n):
#     sieve = [True] * n
#
#     m = int(n ** 0.5)
#     for a in range(2, m + 1):
#         if sieve[a]:
#             for b in range(a+a, n, a):
#                 sieve[b] = False
#
#     return [i for i in range(2, n) if sieve[i]]
#
#
# arr = prime_list(y+1)[len(prime_list(x)):]
#
# for i in arr:
#     print(i)

# 10773 제로

# k = int(input())
# arr = []
#
# for i in range(k):
#     a = int(input())
#     if a:
#         arr.append(a)
#     else:
#         arr.pop()
#
# print(sum(arr))


# 1966 프린터 큐

# from collections import deque
#
# a = int(input())
#
# for i in range(a):
#     queue = deque()
#     count = 0
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for j in arr:
#         queue.append(j)
#     while True:
#         if queue[0] == max(queue):
#             queue.popleft()
#             count += 1
#             if m == 0:
#                 break
#             else:
#                 m -= 1
#         else:
#             queue.append(queue.popleft())
#             if m == 0:
#                 m = len(queue)-1
#             else:
#                 m -= 1
#     print(count)


# 11866 요세푸스 문제 0

# from collections import deque
#
# queue = deque()
# arr = []
#
# n, k = map(int, input().split())
#
# for i in range(1, n+1):
#     queue.append(i)
#
# while queue:
#     for i in range(k-1):
#         queue.append(queue.popleft())
#     arr.append(queue.popleft())
#
# print('<'+str(arr)[1:-1]+'>')


# 2108 통계학

# import sys
# import math
# from collections import Counter
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append(int(input()))
#
# c = Counter(arr)
# order = c.most_common()
# maximum = order[0][1]
#
# modes = []
# for num in order:
#     if num[1] == maximum:
#         modes.append(num[0])
#
# modes.sort()
# if len(modes) == 1:
#     c = modes[0]
# else:
#     c = modes[1]
#
# a = round(sum(arr)/n)
# b = sorted(arr)[n//2]
# d = max(arr) - min(arr)
#
# print(a)
# print(b)
# print(c)
# print(d)


# 10989 수 정렬하기 3

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# dic = {}
#
# for i in range(n):
#     a = int(input())
#     if a in dic:
#         dic[a] += 1
#     else:
#         dic[a] = 1
#
# dic_sort = sorted(dic.items())
#
# for i in range(len(dic_sort)):
#     for j in range(dic_sort[i][1]):
#         print(dic_sort[i][0])


# 1874 스택 수열

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# arr2 = []
# result = []
# count = 0
# for i in range(n):
#     arr.append(int(input()))
#
# for i in range(1, n+1):
#     arr2.append(i)
#     result.append('+')
#     while len(arr2) != 0 and arr[count] == arr2[-1]:
#         arr2.pop(-1)
#         result.append('-')
#         count += 1
# if count != len(arr):
#     print('NO')
# else:
#     for i in result:
#         print(i)


# 4949 균형잡힌 세상

# import sys
#
# input = sys.stdin.readline
#
# while True:
#     arr = []
#     text = input().rstrip()
#     confirm = 0
#     for i in range(len(text)):
#         if text[i] == '(':
#             arr.append(1)
#         elif text[i] == ')':
#             if len(arr) == 0 or arr[-1] == 2:
#                 confirm = 1
#                 break
#             if arr[-1] == 1:
#                 arr.pop()
#         elif text[i] == '[':
#             arr.append(2)
#         elif text[i] == ']':
#             if len(arr) == 0 or arr[-1] == 1:
#                 confirm = 1
#                 break
#             if arr[-1] == 2:
#                 arr.pop()
#
#     if text == '.':
#         break
#
#     if len(arr) == 0 and confirm == 0:
#         print('yes')
#     else:
#         print('no')


# 11651 좌표 정렬하기 2

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for i in range(n):
#     a, b = map(int, input().split())
#     arr.append((a, b))
#
# arr.sort(key=lambda x: (x[1], x[0]))
#
# for i in arr:
#     print(i[0], i[1])


# 1764 듣보잡

# n, m = map(int, input().split())
# set_first = set()
# set_second = set()
#
# for i in range(n):
#     set_first.add(input())
#
# for i in range(m):
#     set_second.add(input())
#
# set_result = set.intersection(set_first, set_second)
#
# set_final = sorted(set_result)
#
# print(len(set_final))
# for i in set_final:
#     print(i)


# 11723 집합

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# S = [0] * 21
#
# for i in range(n):
#     a = input().rstrip().split()
#     if len(a) == 2:
#         b = int(a[1])
#     if a[0] == 'add':
#         S[b] = 1
#     elif a[0] == 'remove':
#         S[b] = 0
#     elif a[0] == 'check':
#         if S[b] == 1:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == 'toggle':
#         if S[b] == 1:
#             S[b] = 0
#         else:
#             S[b] = 1
#     elif a[0] == 'all':
#         S = [1] * 21
#     elif a[0] == 'empty':
#         S = [0] * 21
