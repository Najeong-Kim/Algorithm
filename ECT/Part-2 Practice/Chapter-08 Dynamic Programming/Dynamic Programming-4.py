n, m = map(int, input().split())
coin = [0] * n
count = [10001] * 10001
for i in range(n):
    coin[i] = int(input())
    count[coin[i]] = 1

for i in range(m+1):
    for j in range(n):
        if i >= coin[j]:
            count[i] = min(count[i], count[i-coin[j]] + 1)

if count[m] == 10001:
    print(-1)
else:
    print(count[m])
