N = int(input())
points = {}
for _ in range(N):
    x, y = map(int, input().split())
    if y in points:
        points[y].append(x)
    else:
        points[y] = [x]

result = 0
for color in points:
    point_list = points[color]
    point_list.sort()
    for i in range(len(point_list)):
        if i == 0:
            result += point_list[i + 1] - point_list[i]
        elif i == len(point_list) - 1:
            result += point_list[i] - point_list[i - 1]
        else:
            result += min(point_list[i + 1] - point_list[i], point_list[i] - point_list[i - 1])

print(result)