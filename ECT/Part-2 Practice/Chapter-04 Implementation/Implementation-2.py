n, m = map(int, input().split())
a, b, d = map(int, input().split())

gameMap = []

for _ in range(n):
    gameMap.append(list(map(int, input().split())))
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
initial_a = a
initial_b = b
result = 1
count = 0
gameMap[initial_a][initial_b] = 2
stop = 0
while stop == 0:
    while count != 4:
        if d == 3:
            d -= 4
        a = a + direction[d+1][0]
        b = b + direction[d+1][1]
        if gameMap[a][b] == 0:
            gameMap[a][b] = 1
            result += 1
            count = 0
            initial_a = a
            initial_b = b
        else:
            a = initial_a
            b = initial_b
            d += 1
            count += 1
    if d == 3:
        d -= 4
    initial_a = a - direction[d + 1][0]
    initial_b = b - direction[d + 1][1]
    if gameMap[initial_a][initial_b] == 0:
        gameMap[initial_a][initial_b] = 1
        result += 1
        count = 0
    else:
        stop = 1


print(result)
