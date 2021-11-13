# 17626 Four Squares

# import sys
# import math
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = [5] * (n+1)
# arr[0] = 0
# arr[1] = 1
#
# for i in range(2, n + 1):
#     for j in range(1, math.floor(math.sqrt(i)) + 1):
#         arr[i] = min(arr[i], arr[i-(j**2)] + 1)
#
# print(arr[n])


# 10026 적록색약

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = []
# arr_second = []
#
# for _ in range(n):
#     word = input().rstrip()
#     arr2 = []
#     arr2_second = []
#     for i in range(len(word)):
#         arr2.append(word[i])
#         arr2_second.append(word[i])
#     arr.append(arr2)
#     arr_second.append(arr2_second)
#
# queue = deque()
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# count = 0
# count_second = 0
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] != 'S':
#             queue.append([i, j])
#             alpha = arr[i][j]
#             count += 1
#             while queue:
#                 x, y = queue.popleft()
#                 arr[x][y] = 'S'
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                         continue
#                     if arr[nx][ny] == alpha:
#                         arr[nx][ny] = 'S'
#                         queue.append([nx, ny])
#
# for i in range(n):
#     for j in range(n):
#         if arr_second[i][j] == 'G':
#             arr_second[i][j] = 'R'
#
# for i in range(n):
#     for j in range(n):
#         if arr_second[i][j] != 'S':
#             queue.append([i, j])
#             alpha = arr_second[i][j]
#             count_second += 1
#             while queue:
#                 x, y = queue.popleft()
#                 arr_second[x][y] = 'S'
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                         continue
#                     if arr_second[nx][ny] == alpha:
#                         arr_second[nx][ny] = 'S'
#                         queue.append([nx, ny])
#
# print(count)
# print(count_second)


# 2630 색종이 만들기

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr2 = list(map(int, input().split()))
#     arr.append(arr2)
#
# white_paper = 0
# blue_paper = 0
#
#
# def paper(array, N):
#     global white_paper
#     global blue_paper
#     total = 0
#     for j in range(N):
#         total += sum(array[j])
#     if total == N**2:
#         blue_paper += 1
#     elif total == 0:
#         white_paper += 1
#     else:
#         paper([row[0:N // 2] for row in array[0:N // 2]], N // 2)
#         paper([row[0:N // 2] for row in array[N // 2:N]], N // 2)
#         paper([row[N // 2:N] for row in array[0:N // 2]], N // 2)
#         paper([row[N // 2:N] for row in array[N // 2:N]], N // 2)
#
#
# paper(arr, n)
# print(white_paper)
# print(blue_paper)


# 5430 AC

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for i in range(T):
#     p = list(map(str, input().rstrip()))
#     n = int(input())
#     try:
#         arr = deque(list(map(int, input()[1:-2].split(','))))
#     except:
#         arr = deque([])
#     arrow = 1
#     error = 0
#     for j in p:
#         if j == 'R':
#             arrow *= -1
#         elif j == 'D':
#             if len(arr) == 0:
#                 print('error')
#                 error = 1
#                 break
#             elif arrow == 1:
#                 arr.popleft()
#             elif arrow == -1:
#                 arr.pop()
#     if arrow == 1 and len(arr) != 0:
#         result = '['
#         for j in range(len(arr)):
#             result += str(arr[j])
#             if j != len(arr)-1:
#                 result += ','
#         result += ']'
#         print(result)
#     elif arrow == -1 and len(arr) != 0:
#         arr.reverse()
#         result = '['
#         for j in range(len(arr)):
#             result += str(arr[j])
#             if j != len(arr) - 1:
#                 result += ','
#         result += ']'
#         print(result)
#     elif len(arr) == 0 and error == 0:
#         print([])


# 7662 이중 우선순위 큐

# import sys
# from collections import deque
# import bisect
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for _ in range(T):
#     a = int(input())
#     queue = deque()
#     count = {}
#     for _ in range(a):
#         x, y = map(str, input().split())
#         y = int(y)
#         if x == 'I':
#             if y not in count:
#                 bisect.insort_left(queue, y)
#                 count[y] = 1
#             else:
#                 count[y] += 1
#         elif len(queue) > 0 and x == 'D' and y == 1:
#             if count[queue[-1]] == 1:
#                 count.pop(queue[-1])
#                 queue.pop()
#             else:
#                 count[queue[-1]] -= 1
#         elif len(queue) > 0 and x == 'D' and y == -1:
#             if count[queue[0]] == 1:
#                 count.pop(queue[0])
#                 queue.popleft()
#             else:
#                 count[queue[0]] -= 1
#
#     if len(queue) == 0:
#         print('EMPTY')
#     else:
#         print(queue[-1], queue[0])


# 1697 숨바꼭질

# from collections import deque
#
# n, k = map(int, input().split())
#
# queue = deque()
# queue.append(n)
#
# visited = [-1] * 100001
# visited[n] = 0
#
# while True:
#     a = queue.popleft()
#     if k == a:
#         print(visited[a])
#         break
#     if a-1 >= 0:
#         if visited[a-1] == -1:
#             queue.append(a-1)
#             visited[a-1] = visited[a] + 1
#     if a+1 <= 100000:
#         if visited[a+1] == -1:
#             queue.append(a+1)
#             visited[a+1] = visited[a] + 1
#     if a*2 <= 100000:
#         if visited[a*2] == -1:
#             queue.append(a*2)
#             visited[a*2] = visited[a] + 1


# 1780 종이의 개수

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr2 = list(map(int, input().split()))
#     arr.append(arr2)
#
# minus_paper = 0
# zero_paper = 0
# plus_paper = 0
#
#
# def paper(array, N):
#     global minus_paper
#     global zero_paper
#     global plus_paper
#     standard = array[0][0]
#     check = 0
#     for j in range(N):
#         for k in range(N):
#             if standard != array[j][k]:
#                 check = 1
#                 if check:
#                     break
#         if check:
#             break
#     if check:
#         paper([row[0:N // 3] for row in array[0:N // 3]], N // 3)
#         paper([row[0:N // 3] for row in array[N // 3:(N // 3) * 2]], N // 3)
#         paper([row[0:N // 3] for row in array[(N // 3) * 2:N]], N // 3)
#         paper([row[N // 3:(N // 3) * 2] for row in array[0:N // 3]], N // 3)
#         paper([row[N // 3:(N // 3) * 2] for row in array[N // 3:(N // 3) * 2]], N // 3)
#         paper([row[N // 3:(N // 3) * 2] for row in array[(N // 3) * 2:N]], N // 3)
#         paper([row[(N // 3) * 2:N] for row in array[0:N // 3]], N // 3)
#         paper([row[(N // 3) * 2:N] for row in array[N // 3:(N // 3) * 2]], N // 3)
#         paper([row[(N // 3) * 2:N] for row in array[(N // 3) * 2:N]], N // 3)
#     else:
#         if standard == 0:
#             zero_paper += 1
#         elif standard == -1:
#             minus_paper += 1
#         elif standard == 1:
#             plus_paper += 1
#
#
# paper(arr, n)
# print(minus_paper)
# print(zero_paper)
# print(plus_paper)


# 11659 구간 합 구하기 4

# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# arr = list(map(int, input().rstrip().split()))
# arr2 = []
# total = 0
#
# for i in arr:
#     total += i
#     arr2.append(total)
#
# for _ in range(M):
#     i, j = map(int, input().split())
#     if i == 1:
#         print(arr2[j-1])
#     else:
#         print(arr2[j-1] - arr2[i-2])
