def find_prime_number(n):
    arr = [1] * (2 * n + 1)
    arr[0] = 0
    arr[1] = 0
    for i in range(2, 2 * n + 1):
        if arr[i] == 0:
            continue
        else:
            now = i * 2
            while now <= 2 * n:
                arr[now] = 0
                now += i
    return sum(arr) - sum(arr[:(n + 1)])


while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(find_prime_number(n))
