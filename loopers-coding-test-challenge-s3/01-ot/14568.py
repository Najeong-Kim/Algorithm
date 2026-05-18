N = int(input())

count = 0
for taek in range(2, N - 1, 2):
    for nam in range(1, N - 1):
        young = N - taek - nam
        if young <= 0:
            continue
        if nam < (young + 2):
            continue
        count += 1

print(count)