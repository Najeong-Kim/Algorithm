# 9465 스티커

# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for i in range(T):
#     N = int(input())
#     arr1 = list(map(int, input().rstrip().split()))
#     arr2 = list(map(int, input().rstrip().split()))
#     max_arr1 = [0] * 100001
#     max_arr2 = [0] * 100001
#     for n in range(1, N + 1):
#         if n == 1:
#             max_arr1[n] = arr1[n - 1]
#             max_arr2[n] = arr2[n - 1]
#         else:
#             max_arr1[n] = max(max_arr2[n - 1], max_arr2[n - 2]) + arr1[n - 1]
#             max_arr2[n] = max(max_arr1[n - 1], max_arr1[n - 2]) + arr2[n - 1]
#     print(max(max_arr1[N], max_arr2[N]))


# 1629 곱셈

# import sys
#
# input = sys.stdin.readline
#
# A, B, C = map(int, input().rstrip().split())
#
#
# def pow(a, b):
#     if b == 1:
#         return a % C
#     else:
#         temp = pow(a, b//2)
#     if b & 1:
#         return temp * temp * a % C
#     else:
#         return temp * temp % C
#
#
# print(pow(A, B))
