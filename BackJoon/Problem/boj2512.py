import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
start, end = 0, max(arr)

while start != end:
    result = 0
    mid = (start + end) // 2
    for i in arr:
        result += min(mid, i)
    if result > M:
        end = mid
    else:
        start = mid + 1

check = 0
for i in arr:
    check += min(end, i)

if check > M:
    print(end - 1)
else:
    print(end)
