import sys
input = sys.stdin.readline

N = int(input())
count = 2

while N != 1:
    if N % count == 0:
        N = N // count
        print(count)
        count = 2
    else:
        count += 1
