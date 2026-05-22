N, K = map(int, input().split())
stats = [list(map(int, input().split())) for _ in range(N)]

result = 10 ** 9
for i in range(N):
    for j in range(N):
        for k in range(N):
            a, b, c = stats[i][0], stats[j][1], stats[k][2]
            count = 0
            for stat in stats:
                if a >= stat[0] and b >= stat[1] and c >= stat[2]:
                    count += 1
            if count >= K:
                result = min(result, a + b + c)

print(result)