#%%

def ThiredCompare(elem):
    return elem[2]


N=int(input())
totallist=list()

for i in range(0, N):
    smalllist = list(map(int,input().split()))
    smalllist.append(0)
    totallist.append(smalllist)

for i in range(0,N):
    overweight = 0
    for j in range(0, N):
        if i == j:
            continue
        if totallist[j][0] > totallist[i][0] and totallist[j][1] > totallist[i][1]:
            overweight += 1
    totallist[i][2] = overweight + 1

for i in range(0, N):
    print(totallist[i][2], end=' ')
    
