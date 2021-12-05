import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

for i in range(N):
    valA = min(A)
    valB = max(B)
    S += valA * valB
    A.remove(valA)
    B.remove(valB)

print(S)
