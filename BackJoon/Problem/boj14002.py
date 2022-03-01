import sys
input = sys.stdin.readline
import copy

N = int(input())
A = list(map(int, input().split()))
result = [[0, [0]]]
for i in A:
    start, end = 0, len(result) - 1
    if result[end][0] < i:
        new = copy.deepcopy(result[end][1])
        new.append(i)
        result.append([i, new])
    else:
        while start != end:
            mid = (start + end) // 2
            if result[mid][0] >= i:
                end = mid
            else:
                start = mid + 1
        if i <= result[start - 1][0]:
            start -= 1
        result[start][0] = i
        new = copy.deepcopy(result[start - 1][1])
        new.append(i)
        result[start][1] = new

print(len(result) - 1)
print(' '.join(map(str, result[-1][1][1:])))
