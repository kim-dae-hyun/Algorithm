import sys

def sudoku_check(i,j):
    for k in range(9):
        if k != j:
            if board[i][k] == board[i][j]:
                return 0
        if k != i:
            if board[k][j] == board[i][j]:
                return 0
    
    subpart_x = (i //3) * 3
    subpart_y = (j //3) * 3
    for x in range(subpart_x, subpart_x+3):
        for y in range(subpart_y, subpart_y+3):
            if i == x and j == y:
                continue
            if board[x][y] == board[i][j]:
                return 0
    return 1


def find_zero(x,y):
    for i in range(x,9):         
        j = y+1 if i == x else 0
        while j < 9:               
            if board[i][j] == 0:
                return False, i, j
            j += 1
    return True, 0, 0

def sudoku_try(x,y,v):
    board[x][y] = v
    if sudoku_check(x,y) == 0:
        return False

    bFinished, i, j = find_zero(x,y)
    if bFinished == True:        
        return True

    for v in range(1,10):
        if sudoku_try(i,j,v) == True:
            return True
        else:
            board[i][j] = 0
    return False

board = list()
for _ in range(9):
    a = list(map(int, sys.stdin.readline().split()))
    board.append(a)

bfinish = False
for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            for v in range(1,10):

                if sudoku_try(x,y,v) == True:
                    bfinish = True
                    break
                else:
                    board[x][y] = 0
    if bfinish == True:
        break

for x in range(9):
    print(*board[x],end=' \n')

