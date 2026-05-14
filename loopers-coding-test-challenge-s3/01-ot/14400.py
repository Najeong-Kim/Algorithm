n = int(input())
x = []
y = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

px, py = x[(n - 1) // 2], y[(n - 1) // 2]
result = 0
for i in range(n):
    result += abs(px - x[i]) + abs(py - y[i])
print(result)