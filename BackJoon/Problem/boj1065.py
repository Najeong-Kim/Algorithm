N = int(input())
count = 0

for i in range(1, N + 1):
    arr = list(map(int, list(str(i))))
    if len(arr) == 1:
        count += 1
        continue
    step = arr[0] - arr[1]
    check = True
    for j in range(len(arr) - 1):
        if arr[j] - arr[j + 1] != step:
            check = False
            break
    if check:
        count += 1

print(count)
