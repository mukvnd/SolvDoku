def isvalid(board, row, column, solution):
    for i in range(0, 9):
        if (board[row][i]==solution and i!=column):
            return False
        if (board[i][column]==solution and i!=row):
            return False
    for i in range(row - (row%3), row - (row%3) + 3):
        for j in range(column - (column%3), column - (column%3) + 3):
            if (board[i][j] == solution and i!=row and j!=column):
                return False
    return True

def solveboard(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if (board[i][j] == '.'):
                for k in range (1,10):
                    if isvalid(board, i, j, str(k)):
                        board[i][j] = str(k)
                        if (solveboard(board)):
                            return True
                        else:
                            board[i][j] = '.'
                return False
    return True


if __name__=="__main__":
    board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
    solveboard(board)
    a = 0
    for i in board:
        for j in i:
            if j == '.':
                print("Unsolvable sudoku, check the numbers\n")
                a = 1
                break
        if a == 1:
            break
    if a==0:
        print(board)

