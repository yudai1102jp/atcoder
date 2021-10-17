n = 10

board = [[0]*n for i in range(n)]


for i in range(1, n):
    for j in range(1, n):
        if i > j:
            continue
        board[i][j] = 1 if 0 in [k[j] for k in board[:i]] else 0
print(board)
