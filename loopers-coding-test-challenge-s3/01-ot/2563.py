N = int(input())
paper = [[False] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = True

count = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            count += 1

print(count)
