#5397 키로거

# N = int(input())
#
# for i in range(N):
#     text = input()
#     front = []
#     back = []
#     result = ''
#     for j in range(len(text)):
#         if text[j] == '<':
#             if len(front):
#                 back.append(front[-1])
#                 front.pop()
#         elif text[j] == '>':
#             if len(back):
#                 front.append(back[-1])
#                 back.pop()
#         elif text[j] == '-':
#             if len(front):
#                 front.pop()
#         else:
#             front.append(text[j])
#     for j in range(len(front)):
#         result += front[j]
#     for j in range(len(back)):
#         result += back[len(back) - j - 1]
#     print(result)


# 10930 SHA-256

# import hashlib
#
# text = input().rstrip()
#
# print(hashlib.sha256(text.encode()).hexdigest())


# 2750 수 정렬하기

# import sys
# import heapq
# input = sys.stdin.readline
#
# N = int(input())
#
# queue = []
#
# for i in range(N):
#     num = int(input())
#     heapq.heappush(queue, num)
#
# while queue:
#     print(heapq.heappop(queue))


# 1427 소트인사이드

# import sys
# input = sys.stdin.readline
#
# text = input().rstrip()
#
# count = {}
# result = ''
#
# for i in text:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
#
# for i in range(10):
#     check = str(9 - i)
#     if check in count:
#         result += check * count[check]
#
# print(result)


# 2747 피보나치 수

# N = int(input())
#
# arr = [0] * 46
# arr[1] = 1
#
# for i in range(2, N+1):
#     arr[i] = arr[i-1] + arr[i-2]
#
# print(arr[N])
