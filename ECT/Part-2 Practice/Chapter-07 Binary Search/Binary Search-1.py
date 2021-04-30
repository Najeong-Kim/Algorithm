n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
result = ''
a.sort()


def binary_search(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if target == array[mid]:
        return 'yes'
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in range(m):
    result += binary_search(a, b[i], 0, n-1) + ' '

print(result)


