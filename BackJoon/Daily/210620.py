# 9935 문자열 폭발

# import sys
#
# input = sys.stdin.readline
#
# word = input().rstrip()
# bomb = list(map(str, input().rstrip()))
# arr = []
#
# for i in word:
#     arr.append(i)
#     if i == bomb[-1]:
#         if arr[len(arr) - len(bomb):] == bomb:
#             for _ in range(len(bomb)):
#                 arr.pop()
#
# if len(arr) == 0:
#     print('FRULA')
# else:
#     for i in arr:
#         print(i, end='')


# 10830 행렬 제곱

# import sys
#
# input = sys.stdin.readline
#
# N, B = map(int, input().rstrip().split())
# arr = []
#
# for _ in range(N):
#     arr2 = list(map(int, input().rstrip().split()))
#     arr.append(arr2)
#
#
# def times(array1, array2):
#     array = [[0] * N for _ in range(N)]
#     for j in range(N):
#         for k in range(N):
#             for l in range(N):
#                 array[j][k] += array1[j][l] * array2[l][k]
#     return array
#
#
# def square(array, n):
#     if n == 1:
#         for i in range(len(array)):
#             for j in range(len(array[i])):
#                 array[i][j] = array[i][j] % 1000
#         return array
#     else:
#         temp = square(array, n//2)
#     if n & 1:
#         array2 = times(times(temp, temp), array)
#         for i in range(len(array2)):
#             for j in range(len(array2[i])):
#                 array2[i][j] = array2[i][j] % 1000
#         return array2
#     else:
#         array2 = times(temp, temp)
#         for i in range(len(array2)):
#             for j in range(len(array2[i])):
#                 array2[i][j] = array2[i][j] % 1000
#         return array2
#
#
# total = square(arr, B)
#
# for i in range(len(total)):
#     for j in total[i]:
#         print(j % 1000, end=' ')
#     print('')


# 11444 피보나치 수 6

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = [[1, 1], [1, 0]]
#
# N = 2
#
#
# def times(array1, array2):
#     array = [[0] * N for _ in range(N)]
#     for j in range(N):
#         for k in range(N):
#             for l in range(N):
#                 array[j][k] += array1[j][l] * array2[l][k]
#     return array
#
#
# def fibo(n):
#     if n == 0:
#         return [[1, 0], [0, 1]]
#     elif n == 1:
#         return arr
#     else:
#         temp = fibo(n//2)
#         if n % 2 == 0:
#             arr2 = times(temp, temp)
#             for i in range(len(arr2)):
#                 for j in range(len(arr2[i])):
#                     arr2[i][j] = arr2[i][j] % 1000000007
#             return arr2
#         elif n % 2 == 1:
#             arr2 = times(times(temp, temp), arr)
#             for i in range(len(arr2)):
#                 for j in range(len(arr2[i])):
#                     arr2[i][j] = arr2[i][j] % 1000000007
#             return arr2
#
#
# print(fibo(n)[0][1])
