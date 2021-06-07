
def MakeSequence(datalist):
    for i in range(1,N+1):
        datalist.append(i)
        if len(datalist) < M:
            MakeSequence(datalist)
        else:
            print(*datalist)
            datalist.pop()
    if len(datalist) != 0:
        datalist.pop()

datalist = list()
N,M = map(int, input().split())
MakeSequence(datalist)
