N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(1, N):
    total += abs(points[i][0] - points[i - 1][0]) + abs(points[i][1] - points[i - 1][1])

result = total
for i in range(1, N - 1):
    a_to_b = abs(points[i][0] - points[i - 1][0]) + abs(points[i][1] - points[i - 1][1])
    b_to_c = abs(points[i + 1][0] - points[i][0]) + abs(points[i + 1][1] - points[i][1])
    a_to_c = abs(points[i + 1][0] - points[i - 1][0]) + abs(points[i + 1][1] - points[i - 1][1])
    result = min(result, total - a_to_b - b_to_c + a_to_c)

print(result)