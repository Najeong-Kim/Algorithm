N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = -10 ** 9
for i in range(N - K + 1):
    result = max(result, sum(arr[i:i + K]))

print(result)