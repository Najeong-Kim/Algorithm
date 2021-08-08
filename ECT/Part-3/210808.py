# 01 모험가 길드

# N = int(input())
# array = list(map(int, input().split()))
# array.sort()
#
# count = 0
# result = 0
#
# for i in array:
#     count += 1
#     if i <= count:
#         result += 1
#         count = 0
#
# print(result)


# 02 곱하기 혹은 더하기

# S = input()
#
# result = 0
#
# for i in range(len(S)):
#     if result < 2 or int(S[i]) < 2:
#         result += int(S[i])
#     else:
#         result *= int(S[i])
#
# print(result)


# 03 문자열 뒤집기

# S = input()
#
# count1 = 0
# count0 = 0
#
# if S[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(S)-1):
#     if S[i] != S[i+1]:
#         if S[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1
#
# print(min(count1, count0))
