n = int(input())

count = 10 ** 9
for i in range((n // 5) + 1):
    if (n - (5 * i)) % 2 == 0:
        two = (n - (5 * i)) // 2
        count = min(count, i + two)

if count == 10 ** 9:
    print(-1)
else:
    print(count)