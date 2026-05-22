import math

yumi_x, yumi_y = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(3)]

result = 10 ** 9
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i == j or j == k or k == i:
                continue
            first = math.sqrt((yumi_x - points[i][0]) ** 2 + (yumi_y - points[i][1]) ** 2)
            second = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            third = math.sqrt((points[j][0] - points[k][0]) ** 2 + (points[j][1] - points[k][1]) ** 2)
            result = min(result, first + second + third)

print(math.trunc(result))