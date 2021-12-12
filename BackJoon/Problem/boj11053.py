import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
value = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i] and value[j] >= value[i]:
            value[i] = value[j] + 1

print(max(value))
