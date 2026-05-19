N = int(input())
columns = [list(map(int, input().split())) for _ in range(N)]

columns.sort(key=lambda x: x[0])

left = [0] * 1001
right = [0] * 1002

left_index = 0
for i in range(1, 1001):
    if left_index < N and columns[left_index][0] == i:
        left[i] = max(columns[left_index][1], left[i - 1])
        left_index += 1
    else:
        left[i] = left[i - 1]

right_index = N - 1
for i in range(1000, 0, -1):
    if right_index >= 0 and columns[right_index][0] == i:
        right[i] = max(columns[right_index][1], right[i + 1])
        right_index -= 1
    else:
        right[i] = right[i + 1]

result = [0] * 1001
for i in range(1001):
    result[i] = min(left[i], right[i])

print(sum(result))