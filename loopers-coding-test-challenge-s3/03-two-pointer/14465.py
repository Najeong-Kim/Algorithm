N, K, B = map(int, input().split())
arr = []
for i in range(B):
    arr.append(int(input()))
arr.sort()
broken = [0] * (N + 1)
for i in range(B):
    broken[arr[i]] = 1

result = 10 ** 9
count = 0
for i in range(1,1 + K):
    if broken[i]:
        count += 1

result = min(result, count)

for i in range(1, N - K + 1):
    if broken[i]:
        count -= 1
    if broken[i + K]:
        count += 1
    result = min(result, count)

print(result)