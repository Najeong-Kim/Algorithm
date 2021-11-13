# 1904 01타일

# N = int(input())
# arr = [0] * 15746
# arr[0] = 1
# arr[1] = 1
# for i in range(2, N + 1):
#     num = i % 15746
#     arr[num] = (arr[num-2] + arr[num-1]) % 15746
#
# print(arr[N % 15746])


# 13305 주유소

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# distance = list(map(int, input().split()))
# city = list(map(int, input().split()))
# cost = 0
#
# for i in range(N-1):
#     if i > 0 and city[i] > city[i-1]:
#         city[i] = city[i-1]
#     cost += city[i] * distance[i]
#
# print(cost)


# 15649 N과 M (1)

# from itertools import permutations
#
# N, M = map(int, input().split())
#
# arr = []
# for i in range(N):
#     arr.append(i+1)
#
# result = list(permutations(arr, M))
# for i in range(len(result)):
#     word = ''
#     for j in range(len(result[i])):
#         word += str(result[i][j]) + ' '
#     print(word)
