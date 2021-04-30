n, m = map(int, input().split())
rice = list(map(int, input().split()))
rice.sort()

cutting = 0
maxRice = rice[len(rice)-1]

while True:
    for i in rice:
        cut = i - maxRice
        if cut >= 0:
            cutting += cut
    if m <= cutting:
        break
    else:
        maxRice -= 1
        cutting = 0

print(maxRice)
