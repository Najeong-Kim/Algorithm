N = int(input())

result = 0


def put_queen(arr):
    global result
    now_col = len(arr)
    if now_col == N:
        result += 1
    else:
        for now_row in range(N):
            now = (now_row, now_col)
            check = True
            for (row, col) in arr:
                distance = now_col - col
                if now_row == row:
                    check = False
                    break
                elif row + distance == now_row or row - distance == now_row:
                    check = False
                    break
            if check is True:
                arr.append(now)
                put_queen(arr)
                arr.remove(now)


for init in range(N):
    put_queen([(init, 0)])
print(result)
