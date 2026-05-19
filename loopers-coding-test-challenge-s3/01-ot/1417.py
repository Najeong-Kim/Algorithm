N = int(input())
votes = [int(input()) for _ in range(N)]

count = 0
while True:
    ok = True
    for i in range(1, N):
        if votes[0] <= votes[i]:
            ok = False
    if ok:
        break

    max_vote = max(votes)
    for i in range(1, N):
        if votes[i] == max_vote:
            votes[0] += 1
            votes[i] -= 1
            count += 1
            break

print(count)