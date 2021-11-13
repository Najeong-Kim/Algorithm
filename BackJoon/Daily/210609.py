# 2775 부녀회장이 될테야

# test = int(input())
#
# for _ in range(test):
#     k = int(input())
#     n = int(input())
#     arr = []
#     for i in range(k+1):
#         arr2 = []
#         for j in range(n):
#             if i == 0:
#                 arr2.append(j+1)
#             else:
#                 arr2.append(sum(arr[i-1][0:j+1]))
#         arr.append(arr2)
#     print(arr[k][n-1])


# 2798 블랙잭

# n, m = map(int, input().split())
# inputArr = list(map(int, input().split()))
# maxNum = 0
#
#
# def gen_combinations(arr, count):
#     result = []
#
#     if count == 0:
#         return [[]]
#
#     for i in range(0, len(arr)):
#         elem = arr[i]
#         rest_arr = arr[i + 1:]
#         for C in gen_combinations(rest_arr, count-1):
#             result.append([elem] + C)
#
#     return result
#
#
# sumArr = gen_combinations(inputArr, 3)
# newArr = []
#
# for i in sumArr:
#     count = 0
#     for j in i:
#         count += j
#     newArr.append(count)
#
# for i in newArr:
#     if maxNum < i <= m:
#         maxNum = i
#
# print(maxNum)


# 2839 설탕 배달

# n = int(input())
# result = -1
#
# for i in range(5):
#     if (n - 3 * i) >= 0 and (n - 3 * i) % 5 == 0:
#         result = (n - 3 * i) // 5 + i
#         break
#
# print(result)


# 2869 달팽이는 올라가고 싶다

# a, b, v = map(int, input().split())
#
# initial = (v - a) // (a-b)
# if (v - a) % (a - b) != 0:
#     initial += 1
#
# print(initial + 1)


# 4153 직각삼각형

# while True:
#     a, b, c = map(int, input().split())
#     k = max(a, b, c)
#     if a == 0 and b == 0 and c == 0:
#         break
#     if a*a + b*b == k*k or b*b + c*c == k*k or c*c + a*a == k*k:
#         print('right')
#     else:
#         print('wrong')


# 10250 ACM 호텔

# T = int(input())
#
# for i in range(T):
#     H, W, N = map(int, input().split())
#     if N % H == 0:
#         first = str(H)
#     else:
#         first = str(N % H)
#     if N == 1:
#         second = '01'
#     elif ((N-1) // H) + 1 < 10:
#         second = '0' + str(((N-1) // H) + 1)
#     else:
#         second = str(((N-1) // H) + 1)
#     print(first + second)


# 11050 이항 계수 1

# n, k = map(int, input().split())
# a = 1
#
# for i in range(k):
#     a *= (n-i)/(i+1)
#
# print(int(a))


# 15829 Hashing

# n = int(input())
# text = input()
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# result = 0
#
# for i in range(len(text)):
#     result += (alphabet.index(text[i])+1) * 31**i
#
# print(result % 1234567891)


# 1181 단어 정렬

# n = int(input())
# dic = {}
#
# for _ in range(n):
#     a = input()
#     dic[a] = len(a)
#
# dic_items = sorted(dic.items())
# dic_items2 = sorted(dic_items, key=lambda x: x[1])
#
# for i in dic_items2:
#     print(i[0])


# 1920 수 찾기

# import sys
#
# input = sys.stdin.readline
#
# n = input().split()[0]
# A = input().rstrip().split()
# m = input().split()[0]
# B = input().rstrip().split()
#
# arr = set(A)
#
# for i in B:
#     if i in arr:
#         print(1)
#     else:
#         print(0)


# 1978 소수 찾기

# n = int(input())
# A = list(map(int, input().split()))
# result = 0
# for i in A:
#     count = 0
#     if i == 1:
#         continue
#     for j in range(2, i):
#         if i % j == 0:
#             count += 1
#     if count == 0:
#         result += 1
#
# print(result)


# 2164 카드2

# from collections import deque
#
# n = int(input())
# queue = deque([])
#
# for i in range(1, n+1):
#     queue.append(i)
#
# while len(queue) != 1:
#     queue.popleft()
#     queue.append(queue.popleft())
#
# print(queue.popleft())


# 2609 최대공약수와 최소공배수

# a, b = map(int, input().split())
# c = 0
#
# for i in range(a):
#     if a % (a-i) == 0 and b % (a-i) == 0:
#         c = a-i
#         break
#
# print(c)
# print(int(a*b/c))


# 2751 수 정렬하기 2

# import sys
#
# input = sys.stdin.readline
#
# arr = []
# n = int(input())
#
# for i in range(n):
#     arr.append(int(input()))
#
# arr.sort()
#
# for i in range(n):
#     print(arr[i])


# 9012 괄호

# T = int(input())
#
# for i in range(T):
#     a = input()
#     count = 0
#     for j in range(len(a)):
#         if a[j] == '(':
#             count += 1
#         elif a[j] == ')':
#             count -= 1
#         if count < 0:
#             print('NO')
#             break
#     if count == 0:
#         print('YES')
#     elif count > 0:
#         print('NO')


# 10814 나이순 정렬

# n = int(input())
# arr = []
#
# for i in range(n):
#     a, b = map(str, input().split())
#     a = int(a)
#     arr.append([a, b])
#
# arr.sort(key=lambda x: x[0])
#
# for i in range(n):
#     print(arr[i][0], arr[i][1])


# 10816 숫자 카드 2

# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# arr2 = list(map(int, input().split()))
#
# dic = {}
#
# for i in arr:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
# for i in arr2:
#     if i in dic:
#         print(dic[i], end=' ')
#     else:
#         print(0, end=' ')


# 10828 스택

# import sys
#
# n = int(sys.stdin.readline())
#
# arr = []
# for i in range(n):
#     a = sys.stdin.readline().split()
#     if a[0] == 'push':
#         arr.append(int(a[1]))
#     elif a[0] == 'pop':
#         if len(arr) == 0:
#             print(-1)
#         else:
#             print(arr.pop())
#     elif a[0] == 'size':
#         print(len(arr))
#     elif a[0] == 'empty':
#         if len(arr) == 0:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == 'top':
#         if len(arr) == 0:
#             print(-1)
#         else:
#             print(arr[-1])


# 10845 큐

# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
#
# queue = deque()
#
# for i in range(n):
#     a = sys.stdin.readline().split()
#     if a[0] == 'push':
#         queue.append(int(a[1]))
#     elif a[0] == 'pop':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue.popleft())
#     elif a[0] == 'size':
#         print(len(queue))
#     elif a[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif a[0] == 'back':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])


# 10866 덱

# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
#
# queue = deque()
#
# for i in range(n):
#     a = sys.stdin.readline().split()
#     if a[0] == 'push_front':
#         queue.appendleft(int(a[1]))
#     elif a[0] == 'push_back':
#         queue.append(int(a[1]))
#     elif a[0] == 'pop_front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue.popleft())
#     elif a[0] == 'pop_back':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue.pop())
#     elif a[0] == 'size':
#         print(len(queue))
#     elif a[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif a[0] == 'back':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])


# 11650 좌표 정렬하기

# n = int(input())
# arr = []
# for i in range(n):
#     a, b = map(int, input().split())
#     arr.append((a, b))
#
# arr.sort(key=lambda x: (x[0], x[1]))
#
# for i in arr:
#     print(i[0], i[1])
