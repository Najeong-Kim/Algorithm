arr = [False for i in range(10001)]


def d(number):
    result = number
    times = len(str(number))
    for i in range(times):
        result += int(str(number)[i])
    return result


for i in range(1, 10001):
    now = i
    while True:
        now = d(now)
        if now <= 10000 and arr[now] is False:
            arr[now] = True
        else:
            break

for i in range(1, 10001):
    if arr[i] is False:
        print(i)
