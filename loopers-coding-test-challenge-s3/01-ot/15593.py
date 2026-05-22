N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    now = [0] * 1000
    for j in range(N):
        if i == j:
            continue
        for k in range(times[j][0], times[j][1]):
            now[k] = 1
    result = max(result, sum(now))

print(result)