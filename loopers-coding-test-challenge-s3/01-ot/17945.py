a, b = map(int, input().split())

result = []

for i in range(-1000000, 1000001):
    if (i ** 2 + 2 * a * i + b) == 0:
        print(i, end=' ')

print(" ".join(result))