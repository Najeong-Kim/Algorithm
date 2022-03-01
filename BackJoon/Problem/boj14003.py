import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = [-1000000001]
index = [0] * (len(A) + 1)
for i in range(len(A)):
    start, end = 0, len(result) - 1
    if result[end] < A[i]:
        result.append(A[i])
        index[i + 1] = len(result) - 1
    else:
        while start != end:
            mid = (start + end) // 2
            if result[mid] >= A[i]:
                end = mid
            else:
                start = mid + 1
        if A[i] <= result[start - 1]:
            start -= 1
        result[start] = A[i]
        index[i + 1] = start

print(len(result) - 1)
check = len(result) - 1
answer = []
for i in reversed(range(len(index))):
    if index[i] == check and check != 0:
        answer.append(A[i - 1])
        check -= 1

print(' '.join(map(str, reversed(answer))))
