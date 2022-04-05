list_x = {}
list_y = {}

result_x = 0
result_y = 0

for i in range(3):
    x, y = map(int, input().split())
    if x not in list_x:
        list_x[x] = 1
    else:
        list_x[x] += 1
    if y not in list_y:
        list_y[y] = 1
    else:
        list_y[y] += 1

for i in list_x:
    if list_x[i] == 1:
        result_x = i

for i in list_y:
    if list_y[i] == 1:list_x = {}
list_y = {}

result_x = 0
result_y = 0

for i in range(3):
    x, y = map(int, input().split())
    if x not in list_x:
        list_x[x] = 1
    else:
        list_x[x] += 1
    if y not in list_y:
        list_y[y] = 1
    else:
        list_y[y] += 1

for i in list_x:
    if list_x[i] == 1:
        result_x = i

for i in list_y:
    if list_y[i] == 1:
        result_y = i

print(result_x, result_y)

        result_y = i

print(result_x, result_y)
