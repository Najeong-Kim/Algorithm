X = int(input())

n = 1
while (n * (n-1)/2) < X:
    n += 1

step = int(X - ((n-1) * (n-2)/2))

if n % 2 == 1:
    print(str(step) + '/' + str(n - step))
else:
    print(str(n - step) + '/' + str(step))
