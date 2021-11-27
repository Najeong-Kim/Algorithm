import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
acc = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            acc[i][j] = arr[i][j]
        elif i == 0:
            acc[i][j] = acc[i][j-1] + arr[i][j]
        elif j == 0:
            acc[i][j] = acc[i-1][j] + arr[i][j]
        else:
            acc[i][j] = acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1] + arr[i][j]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    I, J, X, Y = i-1, j-1, x-1, y-1
    if I == 0 and J == 0:
        print(acc[X][Y])
    elif I == 0:
        print(acc[X][Y] - acc[X][J-1])
    elif J == 0:
        print(acc[X][Y] - acc[I-1][Y])
    else:
        print(acc[X][Y] - acc[X][J-1] - acc[I-1][Y] + acc[I-1][J-1])
