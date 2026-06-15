N = int(input())
a = input()
b = input()

count = 0
isConnected = False
for i in range(N):
    if a[i] == b[i]:
        isConnected = False
    else:
        if not isConnected:
            count += 1
            isConnected = True

print(count)