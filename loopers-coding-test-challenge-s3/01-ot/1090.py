N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

x_list = list(map(lambda x: x[0], points))
y_list = list(map(lambda x: x[1], points))


result = [10 ** 9] * N
for x in x_list:
    for y in y_list:
        now_list = []
        for i in range(len(points)):
            dx = abs(points[i][0] - x)
            dy = abs(points[i][1] - y)
            now_list.append(dx + dy)
        now_list.sort()
        sum_value = 0
        for i in range(len(now_list)):
            sum_value += now_list[i]
            result[i] = min(result[i], sum_value)

print(' '.join(map(str, result)))