n, m = map(int, input().split())

iceList = []

for _ in range(n):
    iceList.append(list(map(int, input().split())))

count = 0


def bfs(ice, i, j):
    if i >= n or j >= m:
        return
    elif ice[i][j] == 0:
        ice[i][j] = 1
        bfs(ice, i+1, j)
        bfs(ice, i, j+1)


for one in range(n):
    for two in range(m):
        if iceList[one][two] == 0:
            bfs(iceList, one, two)
            count += 1

print(iceList)
print(count)


