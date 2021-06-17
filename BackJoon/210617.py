# 1157 단어 공부

# a = input().upper()
# arr = {}
#
# for i in a:
#     if i not in arr:
#         arr[i] = 1
#     elif i in arr:
#         arr[i] += 1
#
# arr_sorted = sorted(arr.items(), key=lambda x: x[1], reverse=True)
#
# if len(arr) > 1 and arr_sorted[0][1] == arr_sorted[1][1]:
#     print('?')
# else:
#     print(arr_sorted[0][0])


# 1181 단어 정렬

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# li = set()
#
# for _ in range(n):
#     a = input().rstrip()
#     li.add(a)
#
# li_sorted = sorted(li, key=lambda x: (len(x), x))
#
# for i in li_sorted:
#     print(i)


# 15650 N과 M (2)

# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# N, M = map(int, input().rstrip().split())
# arr = []
#
# for i in range(1, N + 1):
#     arr.append(i)
#
# arr_com = list(combinations(arr, M))
#
# for i in arr_com:
#     for j in i:
#         print(j, end=' ')
#     print('')


# 15652 N과 M (4)

# import sys
# from itertools import combinations_with_replacement
#
# input = sys.stdin.readline
#
# N, M = map(int, input().rstrip().split())
# arr = []
#
# for i in range(1, N + 1):
#     arr.append(i)
#
# arr_com = list(combinations_with_replacement(arr, M))
#
# for i in arr_com:
#     for j in i:
#         print(j, end=' ')
#     print('')


# 15654 N과 M (5)

# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# N, M = map(int, input().rstrip().split())
# arr = list(map(int, input().rstrip().split()))
#
# arr.sort()
#
# arr_com = list(permutations(arr, M))
#
# for i in arr_com:
#     for j in i:
#         print(j, end=' ')
#     print('')


# 15657 N과 M (8)

# import sys
# from itertools import combinations_with_replacement
#
# input = sys.stdin.readline
#
# N, M = map(int, input().rstrip().split())
# arr = list(map(int, input().rstrip().split()))
#
# arr.sort()
#
# arr_com = list(combinations_with_replacement(arr, M))
#
# for i in arr_com:
#     for j in i:
#         print(j, end=' ')
#     print('')


# 15663 N과 M (9)

# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# N, M = map(int, input().rstrip().split())
# arr = list(map(int, input().rstrip().split()))
#
# arr_com = list(permutations(arr, M))
# result = set()
#
# for i in arr_com:
#     result.add(i)
#
# for i in range(1, len(arr_com[0]) + 1):
#     result = sorted(result, key= lambda x: x[-i])
#
# for i in result:
#     for j in i:
#         print(j, end=' ')
#     print('')


# 15666 N과 M (12)

# import sys
# from itertools import combinations_with_replacement
#
# input = sys.stdin.readline
#
# N, M = map(int, input().rstrip().split())
# arr = list(map(int, input().rstrip().split()))
#
# arr.sort()
#
# arr_com = list(combinations_with_replacement(arr, M))
# result = set()
#
# for i in arr_com:
#     result.add(i)
#
# for i in range(1, len(arr_com[0]) + 1):
#     result = sorted(result, key= lambda x: x[-i])
#
# for i in result:
#     for j in i:
#         print(j, end=' ')
#     print('')

