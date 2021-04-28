from collections import deque

n, m = map(int, input().split())

mapList = [list(map(int, input())) for _ in range(n)]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    mapList[i][j] = 0
    count = 1
    while queue:
        i, j = queue.popleft()
        check = 0
        if i+1 < n and mapList[i+1][j] == 1:
            mapList[i+1][j] = 0
            queue.append((i+1, j))
            count += 1
            check += 1
        if j+1 < m and mapList[i][j+1] == 1:
            mapList[i][j + 1] = 0
            queue.append((i, j+1))
            count += 1
            check += 1
        if i-1 >= 0 and mapList[i-1][j] == 1:
            mapList[i-1][j] = 0
            queue.append((i-1, j))
            count += 1
            check += 1
        if j-1 >= 0 and mapList[i][j-1] == 1:
            mapList[i][j - 1] = 0
            queue.append((i, j-1))
            count += 1
            check += 1
        if check == 0:
            count -= 1
        if i == n-1 and j == m-1:
            while queue:
                queue.popleft()
                count -= 1
            return count


print(bfs(0, 0))
