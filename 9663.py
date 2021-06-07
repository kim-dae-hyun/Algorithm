
def promising(cdx):
	for i in range(cdx):
		if board[cdx] == board[i] or cdx - i == abs(board[cdx] - board[i]):
			return 0
	return 1

def nqueen(cdx):
    global count
    if cdx == N:
        count += 1
        return 1
    for i in range(N):
        board[cdx] = i
        if promising(cdx) == 1:
            nqueen(cdx+1)


N=int(input())
count = 0
board= [-1] * N
nqueen(0)
print(count)


