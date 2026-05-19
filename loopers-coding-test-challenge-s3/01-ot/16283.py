a, b, n, w = map(int, input().split())

result = []

for i in range(1, n):
    sheep, goat = i, n - i
    if a * sheep + b * goat == w:
        result.append((sheep, goat))

if len(result) == 1:
    print(result[0][0], result[0][1])
else:
    print(-1)