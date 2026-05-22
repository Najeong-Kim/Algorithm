import copy

board = [list(input()) for _ in range(10)]

def check_win(board):
    for i in range(10):
        for j in range(10):
            if i <= 10 - 5:
                if board[i][j] == 'X' and board[i + 1][j] == 'X' and board[i + 2][j] == 'X' and board[i + 3][j] == 'X' and board[i + 4][j] == 'X':
                    return True
            if j <= 10 - 5:
                if board[i][j] == 'X' and board[i][j + 1] == 'X' and board[i][j + 2] == 'X' and board[i][j + 3] == 'X' and board[i][j + 4] == 'X':
                    return True
            if i <= 10 - 5 and j <= 10 - 5:
                if board[i][j] == 'X' and board[i + 1][j + 1] == 'X' and board[i + 2][j + 2] == 'X' and board[i + 3][j + 3] == 'X' and board[i + 4][j + 4] == 'X':
                    return True
            if i <= 10 - 5 and j >= 4:
                if board[i][j] == 'X' and board[i + 1][j - 1] == 'X' and board[i + 2][j - 2] == 'X' and board[i + 3][j - 3] == 'X' and board[i + 4][j - 4] == 'X':
                    return True
    return False


isPossible = 0
for i in range(10):
    if isPossible:
        break
    for j in range(10):
        if isPossible:
            break
        if board[i][j] == '.':
            now_board = copy.deepcopy(board)
            now_board[i][j] = 'X'
            if check_win(now_board):
                isPossible = 1

print(isPossible)