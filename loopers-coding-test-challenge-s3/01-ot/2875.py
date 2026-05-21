N, M, K = map(int, input().split())

count = 0
for i in range(K + 1):
    first = max(0, N - i)
    second = max(0, M - (K - i))
    count = max(count, min(first // 2, second))

print(count)