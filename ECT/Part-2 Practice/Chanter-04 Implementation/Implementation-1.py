n = input()

columnList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
initial_column = columnList.index(n[0])
initial_row = int(n[1])

count = 0
for i in range(8):
    row = initial_row
    column = initial_column
    if i == 0:
        row += 2
        column += 1
    elif i == 1:
        row += 2
        column += -1
    elif i == 2:
        row += -2
        column += 1
    elif i == 3:
        row += -2
        column += -1
    elif i == 4:
        row += 1
        column += 2
    elif i == 5:
        row += 1
        column += -2
    elif i == 6:
        row += -1
        column += 2
    elif i == 7:
        row += -1
        column += -2
    if row > 0 and row <= 8 and column >= 0 and column < 8:
        count += 1

print(count)
