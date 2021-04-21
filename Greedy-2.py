n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

minNums = []

for i in range(n):
    minNum = 100
    for j in data[i]:
        minNum = min(minNum, j)
    minNums.append(minNum)

maxNum = 0
for k in minNums:
    maxNum = max(maxNum, k)

print(maxNum)


