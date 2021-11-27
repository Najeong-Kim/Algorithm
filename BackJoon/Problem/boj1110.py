N = int(input())
result = N
count = 1
while True:
    result = result % 10 * 10 + (result // 10 + result % 10) % 10
    if result == N:
        break
    else:
        count += 1

print(count)
