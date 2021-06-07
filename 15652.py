
def MakeSequence(datalist):
    for i in range(1,N+1):
        if len(datalist) > 0:
            if i < next(iter(datalist[-1:]), 0):
                continue
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

