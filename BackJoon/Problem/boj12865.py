import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * (K + 1)

for i in range(N):
    W, V = map(int, input().split())
    for j in reversed(range(K + 1 - W)):
        arr[W + j] = max(arr[W + j], arr[j] + V)

print(max(arr))
