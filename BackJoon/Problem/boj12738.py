import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = [-1000000001]
for i in A:
    start, end = 0, len(result) - 1
    if result[end] < i:
        result.append(i)
    else:
        while start != end:
            mid = (start + end) // 2
            if result[mid] >= i:
                end = mid
            else:
                start = mid + 1
        if i <= result[start - 1]:
            start -= 1
        result[start] = i

print(len(result) - 1)
