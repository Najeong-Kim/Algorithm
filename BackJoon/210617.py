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
