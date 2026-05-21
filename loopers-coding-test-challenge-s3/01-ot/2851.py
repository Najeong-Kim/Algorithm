arr = [int(input()) for _ in range(10)]

result = 0
for i in range(11):
    now = sum(arr[:i])
    if (abs(now - 100) <= abs(result - 100)):
        result = now

print(result)