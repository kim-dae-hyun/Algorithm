
N = int(input())
listdata = list()
for i in range(N):
    listdata.append(int(input()))

listdata.sort()
for i in range(len(listdata)):
    print(listdata[i])