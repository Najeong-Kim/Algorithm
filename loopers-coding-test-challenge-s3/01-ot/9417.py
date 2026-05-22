import math

N = int(input())

for _ in range(N):
    M = list(map(int, input().split()))
    result = 0
    for i in range(len(M)):
        for j in range(i + 1, len(M)):
            result = max(result, math.gcd(M[i], M[j]))
    print(result)