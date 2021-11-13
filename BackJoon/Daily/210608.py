# 1000 A+B

# a, b = map(int, input().split())
# print(a + b)


# 1001 A-B

# a, b = map(int, input().split())
# print(a - b)


# 1008 A/B

# a, b = map(int, input().split())
# print(a / b)


# 1152 단어의 개수

# arr = list(map(str, input().split()))
# print(len(arr))


# 1157 단어 공부

# a = input().upper()
# arr = {}
# val = []
# for i in range(len(a)):
#     if a[i] not in arr:
#         arr[a[i]] = 1
#     elif a[i] in arr:
#         arr[a[i]] += 1
# for i in arr:
#     val.append(arr[i])
# val.sort(reverse=True)
# if len(val) > 1 and val[0] == val[1]:
#     print('?')
# else:
#     print(max(arr, key=arr.get))


# 1330 두 수 비교하기

# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# elif a == b:
#     print('==')


# 1546 평균

# n = int(input())
# arr = list(map(int, input().split()))
# score = 0
#
# for i in arr:
#     score += (i / max(arr))
#
# print((score/n)*100)


# 2438 별 찍기 - 1

# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     print('')


# 2439 별 찍기 - 2

# n = int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ', end='')
#     for j in range(i+1):
#         print('*', end='')
#     print('')


# 2475 검증수

# a, b, c, d, e = map(int, input().split())
#
# print((a*a + b*b + c*c + d*d + e*e) % 10)


# 2557 Hello World

# print('Hello World!')


# 2562 최댓값

# maxNum = 0
# maxIndex = 0
#
# for i in range(1, 10):
#     a = int(input())
#     if maxNum < a:
#         maxNum = a
#         maxIndex = i
#
# print(maxNum)
# print(maxIndex)


# 2577 숫자의 개수

# multiple = 1
#
# for i in range(3):
#     multiple *= int(input())
#
# multiple = str(multiple)
#
# for i in range(10):
#     count = 0
#     for j in range(len(multiple)):
#         if multiple[j] == str(i):
#             count += 1
#     print(count)


# 2675 문자열 반복

# n = int(input())
# arr = []
# for i in range(n):
#     a, b = input().split()
#     a = int(a)
#     arr.append([a, b])
# for i in range(n):
#     for j in range(len(arr[i][1])):
#         for k in range(arr[i][0]):
#             print(arr[i][1][j], end='')
#     print('')


# 2739 구구단

# n = int(input())
#
# for i in range(1, 10):
#     print(str(n) + ' * ' + str(i) + ' = ' + str(n * i))


# 2741 N 찍기

# n = int(input())
#
# for i in range(1, n + 1):
#     print(i)


# 2742 기찍 N

# n = int(input())
#
# for i in range(1, n + 1):
#     print(n - i + 1)


# 2753 윤년

# n = int(input())
#
# if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
#     print(1)
# else:
#     print(0)


# 2884 알람 시계

# a, b = map(int, input().split())
#
# if b >= 45:
#     print(a, b-45)
# elif b < 45:
#     b = b + 15
#     if a == 0:
#         a = 23
#         print(a, b)
#     else:
#         a = a - 1
#         print(a, b)


# 2908 상수

# a, b = map(str, input().split())
#
# if int(a[2]) > int(b[2]):
#     print(int(a[2]+a[1]+a[0]))
# elif int(a[2]) < int(b[2]):
#     print(int(b[2]+b[1]+b[0]))
# elif int(a[1]) > int(b[1]):
#     print(int(a[2]+a[1]+a[0]))
# elif int(a[1]) < int(b[1]):
#     print(int(b[2]+b[1]+b[0]))
# elif int(a[0]) > int(b[0]):
#     print(int(a[2]+a[1]+a[0]))
# elif int(a[0]) < int(b[0]):
#     print(int(b[2]+b[1]+b[0]))


# 2920 음계

# arr = list(map(int, input().split()))
#
# if arr == [1, 2, 3, 4, 5, 6, 7, 8]:
#     print('ascending')
# elif arr == [8, 7, 6, 5, 4, 3, 2, 1]:
#     print('descending')
# else:
#     print('mixed')


# 3052 나머지

# arr = []
# rest = []
#
# for i in range(10):
#     arr.append(int(input()))
# for i in range(10):
#     if arr[i] % 42 not in rest:
#         rest.append(arr[i] % 42)
#
# print(len(rest))


# 8958 OX퀴즈

# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append(input())
#
# for i in range(len(arr)):
#     result = 0
#     count = 0
#     for j in range(len(arr[i])):
#         if arr[i][j] == 'O':
#             count += 1
#             result += count
#         elif arr[i][j] == 'X':
#             count = 0
#     print(result)


# 9498 시험 성적

# n = int(input())
#
# if n >= 90:
#     print('A')
# elif n >= 80:
#     print('B')
# elif n >= 70:
#     print('C')
# elif n >= 60:
#     print('D')
# else:
#     print('F')


# 10171 고양이

# print('\    /\\')
# print(" )  ( ')")
# print('(  /  )')
# print(' \(__)|')


# 10172 개

# print('|\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')


# 10809 알파벳 찾기

# word = input()
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# for i in range(len(alphabet)):
#     if alphabet[i] in word:
#         find = 0
#         for j in range(len(word)):
#             if find == 0 and alphabet[i] == word[j]:
#                 alphabet[i] = j
#                 find = 1
#     else:
#         alphabet[i] = -1
#
# for i in alphabet:
#     print(i, end=' ')


# 10818 최소, 최대

# n = int(input())
#
# arr = list(map(int, input().split()))
# arr.sort()
#
# print(arr[0], arr[-1])


# 10869 사칙연산

# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)


# 10871 X보다 작은 수

# a, b = map(int, input().split())
# arr = list(map(int, input().split()))
# arr2 = []
#
# for i in range(a):
#     if arr[i] < b:
#         arr2.append(arr[i])
#
# for i in arr2:
#     print(i, end=' ')


# 10950 A+B - 3

# n = int(input())
# arr = []
# for i in range(n):
#     a, b = map(int, input().split())
#     arr.append([a, b])
#
# for i in range(n):
#     print(arr[i][0] + arr[i][1])


# 10951 A+B - 4

# arr = []
# while True:
#     try:
#         a, b = map(int, input().split())
#         arr.append([a, b])
#     except EOFError:
#         break
#
# for i in range(len(arr)):
#     print(arr[i][0] + arr[i][1])


# 10952 A+B - 5

# arr = []
# while True:
#     a, b = map(int, input().split())
#     arr.append([a, b])
#     if a == 0 and b == 0:
#         break
#
# for i in range(len(arr)-1):
#     print(arr[i][0] + arr[i][1])


# 10998 A×B

# a, b = map(int, input().split())
#
# print(a * b)


# 11654 아스키 코드

# n = input()
#
# print(ord(n))


# 11720 숫자의 합

# n = int(input())
# word = input()
# result = 0
#
# for i in range(len(word)):
#     result += int(word[i])
#
# print(result)


# 1085 직사각형에서 탈출

# x, y, w, h = map(int, input().split())
#
# print(min(w-x, h-y, x, y))


# 1259 팰린드롬수

# arr = []
# while True:
#     a = input()
#     if a == '0':
#         break
#     else:
#         arr.append(a)
#
# for i in range(len(arr)):
#     answer = 'yes'
#     for j in range(len(arr[i]) // 2):
#         if arr[i][j] == arr[i][len(arr[i])-1-j]:
#             continue
#         else:
#             answer = 'no'
#     print(answer)


# 2231 분해합

# n = input()
#
# for i in range(int(n)+1):
#     count = i
#     number = str(i)
#     for j in range(len(number)):
#         count += int(number[j])
#     if count == int(n):
#         print(i)
#         break
#     elif i == int(n):
#         print('0')


# 2292 벌집

# n = int(input())
# count = 0
# nextNum = 1
# while True:
#     if n <= nextNum:
#         print(count+1)
#         break
#     count += 1
#     nextNum = nextNum + 6 * count
