A, B, C, N = map(int, input().split())

result = 0
for i in range(N // A):
    if result:
        break
    for j in range(N // B):
        if result:
            break
        for k in range(N // C):
            if result:
                break
            if (A * i + B * j + C * k) == N:
                result = 1

print(result)