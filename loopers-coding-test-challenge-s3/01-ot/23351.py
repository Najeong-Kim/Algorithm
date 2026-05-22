N, K, A, B = map(int, input().split())
plants = [K] * N

day = 0
while True:
    if 0 in plants:
        break
    day += 1
    min_water = min(plants)
    for i in range(N // A):
        if min_water in plants[i * A:(i + 1) * A]:
            for j in range(i * A, (i + 1) * A):
                plants[j] += B
            break
    for i in range(N):
        plants[i] -= 1

print(day)