n, k = map(int, input().split())

array_a = list(map(int, input().split()))

array_b = list(map(int, input().split()))

for _ in range(k):
    min_a = 10000000
    min_a_index = -1
    max_b = 0
    max_b_index = -1
    for i in range(n):
        if min_a > array_a[i]:
            min_a = array_a[i]
            min_a_index = i
    for j in range(n):
        if max_b < array_b[j]:
            max_b = array_b[j]
            max_b_index = j
    if max_b > min_a:
        array_a[min_a_index] = max_b
        array_b[max_b_index] = min_a

result = 0
for i in range(n):
    result += array_a[i]

print(result)
