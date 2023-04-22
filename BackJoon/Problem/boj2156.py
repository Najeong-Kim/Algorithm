import sys
input = sys.stdin.readline

arr = []
N = int(input())
for i in range(N):
    arr.append(int(input()))

glass = [0] * N

for i in range(N):
    if i == 0:
        glass[0] = arr[0]
    elif i == 1:
        glass[1] = arr[0] + arr[1]
    elif i == 2:
        glass[2] = max(arr[0] + arr[1], arr[0] + arr[2], arr[1] + arr[2])
    else:
        glass[i] = max(glass[i - 1], arr[i] + glass[i - 2], arr[i] + arr[i - 1] + glass[i - 3])

print(glass[N - 1])
