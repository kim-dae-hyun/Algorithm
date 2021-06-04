
def GetWrongColorCount(X,Y):
    dataCnt = 0
    for x in range(X, X+8):
        for y in range(Y, Y+8):
            if (x + y) % 2 == 0:
                if data[x][y] != 'W':
                    dataCnt += 1
            else:
                if data[x][y] != 'B':
                    dataCnt += 1
    if dataCnt > 32 :
        return 64 - dataCnt
    else:
        return dataCnt
                

N, M = map(int, input().split())

data = list()

# data = [[0]*M for i in range(N)]
for i in range(N):
    onerow = list(input())
    data.append(onerow)
subtotal = 0
mincount = 64


for x in range(0, N-7):
    for y in range(0, M-7):
        subtotal = GetWrongColorCount(x,y)
        mincount = min(mincount, subtotal)
print(mincount)



