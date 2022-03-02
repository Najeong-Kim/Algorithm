import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
length = 100001
result = arr[0]
front = 0
end = 0

while True:
    if result >= S:
        length = min(length, end - front + 1)
    if result > S and front < end:
        result -= arr[front]
        front += 1
    else:
        if end < len(arr) - 1:
            end += 1
            result += arr[end]
        else:
            break

if length == 100001:
    print(0)
else:
    print(length)
