
nthnum = list()

N = int(input())
numcnt = 0
i = 666

while True:
    loopnumstr = str(i)
    pos666 = loopnumstr.find('666')
    if pos666 != -1 :
        numcnt += 1
        if numcnt == N:
            print(loopnumstr)
            exit()
    i += 1

