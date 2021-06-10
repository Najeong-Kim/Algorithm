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
