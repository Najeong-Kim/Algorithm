N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
count = 0
now = arr[0]
while s <= e and e < N:
    if now == M:
        count += 1
        e += 1
        if e >= N:
            break
        now += arr[e]
    elif now > M:
        now -= arr[s]
        s += 1
    elif now < M:
        e += 1
        if e >= N:
            break
        now += arr[e]

print(count)